## This script requires "requests": http://docs.python-requests.org/
## To install: pip install requests
from extract import json_extract
import contact_retrieval, os, requests, json
import tkinter as tk


# Top level window
frame = tk.Tk()
frame.title("Ticket Printer")
frame.attributes('-fullscreen', True)


def printInput():
    domain = "(Your Domain Here)" # Just the subdomain, exclude the ".freshdesk.com/api/v2/*"
    password = '(Your Freshdesk Account Passcode here)'
    api_key = "Your FreshDesk API goes here"

    inp = inputtxt.get(1.0, "end-1c")
    r = requests.get(f"https://{domain}.freshdesk.com/api/v2/tickets/" + inp + "?include=conversations", auth = (api_key, password))
    print(str(inp))
    print(str(r))

    if r.status_code == 200:
        
        lbl.config(text = "Provided Input: "+inp)

        json_content = json.loads(r.content)

        # Use this to debug the ticket
        #print("Request processed succesfully, the response is given below. \n" + (json.dumps(json_content, indent=3)))

        notes = json_extract(r.json(), 'body_text')
        
        tech_responsible = 'none'
        
        # Other Fields ( We're using tech responsible for the ticket) can be included. Just use the json_extract function to search for the field you're using
        contact_id = str(json_extract(r.json(), 'requester_id')[0])

        contact_json = requests.get("https://" + domain + ".freshdesk.com/api/v2/contacts/" + contact_id, auth = (api_key, password))

        contact_name = json_extract(contact_json.json(), "name")[0]

        last_note = str(notes[-1])

        description = str(json_extract(r.json(), 'description_text')[0]) 


        ticket_info = ("Ticket Number: " + inp + "\nCustomer: " + contact_name + "\n" + "\n\n\n"  "\n\n\n" + last_note + 'Other Notes\n\n\n\n\n\n' + '\nBackup Needed:')

        # This sends the intended output to the console before sending it to the printer
        print(ticket_info)

        f = open('printer_test.txt', 'w')
        f.write(ticket_info.replace(u'\u200b','*'))
        f.close

        os.startfile("printer_test.txt", "print")
        
    else:

        lbl.config(text = "Ticket printing failed. Check ticket number"+inp)
        print("Failed to read ticket, errors are displayed below, \n")
        response = json.loads(r.content)
        print(response["errors"])
        print("x-request-id : " + str(r.headers['x-request-id']))
        print("Status Code : " + (r.status_code))

# This makes it so enter works as well as clicking on print
def enterInput(event):
    printInput()

# TextBox Creation
inputtxt = tk.Text(frame,
    height = 5,
    width = 20)
inputtxt.pack(padx = 20, pady = 20)

# Button Creation
printButton = tk.Button(frame,
    text = "Print",
    command = printInput)

printButton.pack()


# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack(padx = 5, pady = 5)

frame.bind('<Return>', enterInput)
frame.mainloop()

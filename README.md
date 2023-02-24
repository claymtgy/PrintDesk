# PrintDesk
A simple interface to print ticket information from FreshDesk

We use it to print out receipts to attach to computers to help with organization
of our workflow.

Go into PrintDesk.py, set your domain, passcode, and API key, and you're off to the races!

If you need to get more fields, or custom fields, from FreshDesk, just follow the template of what's there. 
I can help you if you need specific directions. But start by just printing the entire JSON of the ticket to
see what information you can pull from FreshDesk. Then if you search the JSON for the correct label, the extract
module will save all items with that label as a list. 

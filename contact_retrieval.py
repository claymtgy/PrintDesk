from extract import json_extract
import requests

def get_contact_info():
    ticket_json = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ inp + '?include=conversations', auth = (api_key, password))

    contact_id = str(json_extract(ticket_json.json(), 'requester_id')[0])

    contact_json = requests.get("https://" + domain + ".freshdesk.com/api/v2/contacts/" + contact_id, auth = (api_key, password))

    contact_name = json_extract(contact_json.json(), 'name')[0]

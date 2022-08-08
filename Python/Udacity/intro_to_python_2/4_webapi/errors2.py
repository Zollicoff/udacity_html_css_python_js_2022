import requests

def server_status
try:
    r = requests.get('http://www.udacisdfasdf.com')
    print(r.status_code)
except requests.exceptions.ConnectionError:
    print("Could not Connect to Server")

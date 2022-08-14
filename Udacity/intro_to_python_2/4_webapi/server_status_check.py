import requests

def server_status(site):
    try:
        r = requests.get(site)
        print(r.status_code)
    except requests.exceptions.ConnectionError:
        print("Could not Connect to Server")

server_status("https://google.com")


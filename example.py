import requests
import json
import os

payload = {
    'url': 'YOUR WEBHOOK',
    'method': 'POST',
    'headers': {'Content-Type': 'application/json'},
    'data': json.dumps({
        'content': 'Hello :D',
        'username': 'Test-Bot',
        'avatar_url': 'https://example.com/avatar.png' 
    })
}

api_url = 'http://YOUR_URL/forward_request'

response = requests.post(api_url, json=payload)
print(response.text)

os.system("pause")

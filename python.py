import requests

limit = 3
api_url = 'https://icanhazdadjoke.com/slack'.format(limit)
response = requests.get(api_url)
if response.status_code == requests.codes.ok:
    joke = response.json()['attachments'][0]['text']
    print(f"{joke}")
else:
    print("Error:", response.status_code, response.text)
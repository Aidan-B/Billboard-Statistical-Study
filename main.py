token = ""
  
import requests
import json

url = 'https://api.spotify.com/v1/albums'
payload = {'ids': '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'}
headers = {
    'content-type': 'application/json',
    'Authorization': "Bearer {}".format(token)
}

response = requests.get(url, params=payload, headers=headers)

print(response.text)
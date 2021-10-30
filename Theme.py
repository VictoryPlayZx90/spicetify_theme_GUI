from easygui import * 
import time
import subprocess


title = 'first_gui'

msg = 'Pick one.'

choices = ["Dribbblish", "Fluent", "Dreary",]





reply = choicebox(msg, title, choices = choices)

print("You selected: " + reply)


while True:
    if reply in choices:
        subprocess.call ("spicetify config current_theme " + reply , shell=True)
        time.sleep(1)
        subprocess.call ("spicetify apply" , shell=True)
        subprocess.call ("echo n | Powershell -Command \"Invoke-Expression -Command (Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/mrpond/BlockTheSpot/master/install.ps1')\"" , shell=True)
        subprocess.call (r"C:\Users\priyanshu\AppData\Roaming\Spotify\Spotify.exe" , shell=True)
        break
    else: 
        print("Wrong name. Try again")

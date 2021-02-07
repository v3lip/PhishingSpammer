#IMPORTS
import json
import string
import os
import objdict
import random
import platform

#Functions
def drawLine(symbol):
    rows, columns = os.get_terminal_size()
    i = symbol
    for x in range(2, rows):
        i += symbol
    return i

def allign_center(text):
    rows, columns = os.get_terminal_size()
    devided = rows - 1
    return devided

#Clears terminal
if(platform.system() == 'Windows'):
    os.system('cls')
else:
    os.system('clear')

#Terminal header
title = 'Velip Spam Bot - Settings Generator'
print(drawLine('-'))
print(str.center(title, allign_center(title)))
print(drawLine('-'))

#Inputs
#Save file with a custom name
jsonFilename = input('Save file as => ')
#If no filename input, generate one
if jsonFilename == "":
    jsonFilename = "settings_"
    for i in range(6):
        jsonFilename = jsonFilename + random.choice(string.ascii_letters)
        jsonFilename = jsonFilename.lower()

#Checks if filename input has the extension .json
root, ext = os.path.splitext(jsonFilename)
if not ext:
   ext = '.json'
jsonFilename = root + ext

#Inputs
targetUrl = input('Target URL (http://example.com/login.php) => ')
namesJson = input('Names JSON File (If empty = names.json) => ')
if namesJson == "": namesJson = "names.json"
root, ext = os.path.splitext(namesJson)
if not ext:
   ext = '.json'
namesJson = root + ext
passwordsJson = input('Passwords JSON File (If empty = passwords.json) => ')
if passwordsJson == "": passwordsJson = "passwords.json"
#Checks if filename input has the extension .json
root, ext = os.path.splitext(passwordsJson)
if not ext:
   ext = '.json'
passwordsJson = root + ext
postUsername = input('Form username HTML name (If empty = username) => ')
if postUsername == "": postUsername = "username"
postPassword = input('Form password HTML name (If empty = password) => ')
if postPassword == "": postPassword = "password"

#Generation user input to .json file
print('\nGenerating..')
myDictObj = { \
    "title" : "Velips Phising Spam Bot",
    "version" : "V1.4",
    "targetUrl" : targetUrl,
    "namesJson" : namesJson,
    "passwordsJson" : passwordsJson,

    "postUsername" : postUsername,
    "postPassword" : postPassword,
    "domains" : [ 
        "hotmail.com",
        "gmail.com",
        "outlook.com",
        "live.com",
        "email.com",
        "yahoo.com",
        "icloud.com",
        "msn.com",
        "edu.com",
        "free.fr",
        "web.de",
        "mail.ru"
     ]
}

#Puts data in to the json file
with open(jsonFilename, 'w') as outfile:
    json.dump(myDictObj, outfile)

print('\nJSON was saved as {}!'.format(jsonFilename))
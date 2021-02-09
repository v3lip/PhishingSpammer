# IMPORTS
import requests
import os
import random
import string
import json
import shutil
import sys
import platform
from random import randrange

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

#Choose settings file generated from 'settings-generator.py'
settingsfilejson = input('Settings file (If empty = settings.json) => ')
#If user didn't choose a settings file, use 'settings.json' as default
if settingsfilejson == '': settingsfilejson = 'settings.json'

#Checks if filename input has the extension .json
root, ext = os.path.splitext(settingsfilejson)
if not ext:
   ext = '.json'
settingsfilejson = root + ext

#Loads .json files. //Settings, names and passwords
settings = json.loads(open(settingsfilejson).read())
names = json.loads(open(settings['namesJson']).read())
passwords = json.loads(open(settings['passwordsJson']).read())

#Clears terminal
if(platform.system() == 'Windows'):
    os.system('cls')
else:
    os.system('clear')

#Variables/Dicts
domains = settings['domains']
version = settings['version']
url = settings['targetUrl']

#Makes terminal sexy
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
"reset":"\u001b[0m",
}

#Random variables
random.seed = (os.urandom(1024))

#Declares color rules for the terminal
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

#Terminal header
title = 'Velip Spam Bot' + version
print(drawLine('-'))
print(str.center(title, allign_center(title)))
print(str.center('github.com/m0nstechilled/PhishingSpammer', allign_center('github.com/m0nstechilled/PhishingSpammer')))
print(drawLine('-'))

#Int for counting the loop
run = 0

#Program
try:
    while True:
        #Random email generator
        chance = random.randint(1, 100)
        atdomain = '@' + random.choice(domains)

        if 1 <= chance <= 5:
            username = random.choice(names) + atdomain

        if 6 <= chance <= 20:
            name_extra = str(randrange(0, 99))
            username = random.choice(names) + name_extra + atdomain

        if 21 <= chance <= 42:
            name_extra = str(randrange(0, 99))
            username = random.choice(names) + '_' + name_extra + atdomain

        if 43 <= chance <= 50:
            name_extra = str(randrange(0, 99))
            username = random.choice(names) + '_' + random.choice(names) + name_extra + atdomain

        if 51 <= chance <= 70:
            username = random.choice(names) + '.' + random.choice(names) + atdomain

        if 71 <= chance <= 80:
            name_extra = str(randrange(0, 99))
            username = random.choice(names) + random.choice(names) + name_extra + atdomain

        if 81 <= chance <= 100:
            name_extra = str(randrange(0, 99))
            username = random.choice(names) + name_extra + atdomain

        username = username.lower()

        #Picks random password from the Rockyou passwords file
        password = random.choice(passwords)

        #Sending username and password to the victim
        requests.post(url, allow_redirects=False, data={
            settings['postUsername']: username,
            settings['postPassword']: password
        })

        #Prints out current count and username/password sent to the site
        run = run+1
        print (colorText('{}) Sending username [[red]]{}[[reset]] and password [[magenta]]{}[[reset]]..').format(run, username, password))

except KeyboardInterrupt:
    #Shows the total number of spammed login attempts
    print(drawLine('-'))
    print(colorText('Done! Spammed [[red]]{}[[reset]] times to [[red]]{}[[reset]]!'.format(run, url)))
    print(colorText('github.com/m0nstechilled/PhishingSpammer')

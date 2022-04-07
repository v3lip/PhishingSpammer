PhisingSpammerV2 is currently in development!

# PhisingSpammer 1.4
![N|Solid](https://img.shields.io/github/last-commit/v3lip/PhishingSpammer)
![N|Solid](https://img.shields.io/github/followers/v3lip?style=social)


![N|Solid](https://i.imgur.com/E5ltGFC.png)


PhisingSpammer is an automated bot that spam phising sites with just a few clicks!

  - Fully customizable name and password lists
  - An easy to use settings generator that makes life and 'spamming' very easy

## New Features in 1.4!

  - Settings generator that is very automated and easy to use
  - Have multiple names and passwords files that you can easily switch between

### Donate

Want to buy me a coffee?

BTC Address: bc1qfdaysa6u7zclsryfv8gf8ffqknrj07d9dlgayf

![N|Solid](https://i.imgur.com/smX4eoa.png)

## How to use

First we have to generate a settings.json by running the generator. The generator will ask you a couple of questions,
  - 'Save file as =>' - What do you want your settings file to be saved as?
  - 'Target URL =>' - The URL to the login prompt of your target. Example: http://example.com/login.php
  - 'Names JSON File =>' - A list of random names used by the fake email generator
  - 'Passwords JSON File =>' - A list of random passwords used in the password field of the website.
  - 'Form username HTML name =>' - The name attribute of the input 
        example: `<input class="loginField" type="text" name="USERNAME">` <- The last attribute here
  - 'Form password HTML name =>' - The name attribute of the input 
        example: `<input class="loginField" type="password" name="PASSWORD">` <- The last attribute here
        
Now that we have our settings file, we can run the spammer. The spammer will ask you for the settings file you just created. You can type out the name of the file with or without the `.json`
Now click `enter` and you should get something like this! Happy hunting!

  ![N|Solid](https://i.imgur.com/BJQ2ahF.png)

## Installation

Phising Spammer requires [Python 3.8.*](https://www.python.org/) to run.
(Only tested on Python 3.8.5)

Install the dependencies.

Windows:
```sh
$ python -m pip install -r requirements.txt
```

Linux:
```sh
$ pip3 install -r requirements.txt
```


### Development

Want to contribute? Great!
Keep em' coming and I'll take a look at em'!

## Ideas for next update:
### Feel free to add these features yourself!
  - Make it so it finds the name attributes automatically.

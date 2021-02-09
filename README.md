# PhisingSpammer 1.4

![N|Solid](https://i.imgur.com/E5ltGFC.png)


PhisingSpammer is an automated bot that spam phising sites just by a few clicks!

  - Fully customizable name and password lists
  - An easy to use settings generator that makes life and 'spamming' very easy

# New Features in 1.4!

  - Settings generator that is very automated and easy to use
  - Have multiple names and passwords files that you can easily switch between

### Tech

Phising Spammer is written purely in Python, with few libraries which makes it very easy to use and get going.

### How to use

First we have to generate a settings.json by running the generator. The generator will ask you a couple of questions,
  - 'Save file as =>' - What do you want your settings file to be saved as?
  - 'Target URL =>' - The URL to the login prompt of your target. Example: http://example.com/login.php
  - 'Names JSON File =>' - A list of random names used by the fake email generator
  - 'Passwords JSON File =>' - A list of random passwords used in the password field of the website.
  - 'Form username HTML name =>' - The name attribute of the input 
        example: `<input class="loginField" type="text" name="USERNAME">` <- The last attribute here
  - 'Form password HTML name =>' - The name attribute of the input 
        example: `<input class="loginField" type="password" name="PASSWORD">` <- The last attribute here
        
Now that we have our settings file, we can run the spammer.
  - The spammer will ask you for the settings file. You can type out the name of the file with or without the `.json`
  !(https://i.imgur.com/BJQ2ahF.png)

### Installation

Phising Spammer requires [Python 3.8.*](https://www.python.org/) to run.
(Only tested on Python 3.8.5)

Install the dependencies.

```sh
$ python -m pip install requests
$ python -m pip install pytest-shutil
$ python -m pip install objdict
```


### Development

Want to contribute? Great!
Keep em' coming and I'll take a look at em'!

### TODO
  - Make it so it finds the name attributes automatically.

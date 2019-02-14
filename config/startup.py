import configparser, sys, time, os

def createdat():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'LHOST': '0.0.0.0',
        'RHOST': '',
        'LPORT': '8080',
        'RPORT': '',
        'NAME': '',
        'PLATFORM': '',
        'LASTRUN': '',
        'USERLIST': '/usr/bin/wordlist.txt',
        'PASSLIST': '/usr/bin/passlist.txt',
        'URLPATH': '/connect',
        'INTERFACE': 'wlan0',
        'VERSION': ''
        }
    welcometext = """
Welcome to the DarkSpiritz Penetration Testing Framework.

In order to start you must create a default user config.

All it requires from you is a username you'd like to use.
"""
    typinganimation(welcometext)
    enteruser = "Enter Username: "
    name = input("Enter Username: ")
    config['DEFAULT']['NAME'] = str(name)
    platformchecktxt = "Checking Platform..."
    typinganimation(platformchecktxt)
    platform = sys.platform
    config['DEFAULT']['PLATFORM'] = platform
    savedata = "Creating Configuration File.."
    typinganimation(savedata)
    with open("config/userdat.ini", "w") as configfile:
        config.write(configfile)
    time.sleep(3)

def typinganimation(text):
    for char in text:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

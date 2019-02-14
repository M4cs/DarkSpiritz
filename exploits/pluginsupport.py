import sys, os.path, os
from terminaltables import SingleTable

if sys.platform == "linux":
    class colors:
        BLACK  = '\33[30m'
        RED    = '\33[31m'
        GREEN  = '\33[32m'
        YELLOW = '\33[33m'
        BLUE   = '\33[34m'
        VIOLET = '\33[35m'
        BEIGE  = '\33[36m'
        WHITE  = '\33[37m'
        BLACKBG  = '\33[40m'
        REDBG    = '\33[41m'
        GREENBG  = '\33[42m'
        YELLOWBG = '\33[43m'
        BLUEBG   = '\33[44m'
        VIOLETBG = '\33[45m'
        BEIGEBG  = '\33[46m'
        WHITEBG  = '\33[47m'
        END      = '\33[0m'

else:
    class colors:
        BLACK  = ''
        RED    = ''
        GREEN  = ''
        YELLOW = ''
        BLUE   = ''
        VIOLET = ''
        BEIGE  = ''
        WHITE  = ''
        BLACKBG  = ''
        REDBG    = ''
        GREENBG  = ''
        YELLOWBG = ''
        BLUEBG   = ''
        VIOLETBG = ''
        BEIGEBG  = ''
        WHITEBG  = ''
        END      = ''

sys.path.append("..")
import configparser
from configparser import ConfigParser

config = configparser.ConfigParser()
config.read("config/userdat.ini")

def ask(abc):
    key = abc.upper()
    value = config['DEFAULT'][key]
    dat = '%s' % (value)
    return dat

def dashboard():
    table_data = [
        ['Command:', 'Description:'],
        ['set <key>', 'Set config key value'],
        ['execute', 'Execute plugin'],
        ['back', 'Go back to framework'],
        ['session', 'Show configuration']
    ]
    table = SingleTable(table_data)
    print(table.table)
    print("")
    print("Press Enter To Execute Or Use A Command Above")
    print("")
    termname = colors.BLUE + "[" + colors.END + "plugin" + colors.BLUE + "] " + colors.END
    term = input(termname)
    if term == "":
        print("Executing Plugin.\n")
        pass
    elif term[0:7] == "session":
        print("Current Session Info:\n")
        print("-" * 50)
        for key, value in config.items('DEFAULT'):
            pressed = "{0:17s}{1:12s}".format(key,value).upper()
            print(pressed)
            print('-' * 50)
        print(colors.END)
        dashboard()
    elif term[0:7] == "execute":
        print("Executing Plugin.\n")
        pass
    elif term[0:3] == "set":
        if term[4:] == "lhost":
            config['DEFAULT']['LHOST'] = input("\nEnter Value: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif term[0:] == "set lport":
            config['DEFAULT']['LPORT'] = input("\nEnter Value: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif term[4:9] == "rhost":
            config['DEFAULT']['RHOST'] = input("\nEnter Value: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif term[4:9] == "rport":
            config['DEFAULT']['RPORT'] = input("\nEnter Value: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif term[4:12] == "userlist":
            config['DEFAULT']['USERLIST'] = input("\nEnter Directory: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif term[4:12] == "passlist":
            config['DEFAULT']['PASSLIST'] = input("\nEnter Directory: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        elif term[4:13] == "interface":
            config['DEFAULT']['PASSLIST'] = input("\nEnter Interface: ")
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            dashboard()
        else:
            try:
                config['DEFAULT'][term[4:]] = input("\nEnter Value: ")
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                dashboard()
            except IndexError:
                print("Couldn't Find Value")
    elif term[0:4] == "back":
        exit()
    else:
        print("Unknown Command Try Again!")
        dashboard()

def run(cmd):
    x = check_output(cmd, shell=True)
    i = "\033[1m["+colors.G+"!]"+colors.W+""
    print(i + x)

def warning(msg):
    print("\033[1m"+colors.O+"[/]"+colors.W+"", msg)

def fail(msg):
    print("\033[1m"+colors.R+"[!]"+colors.W+"", msg)

def success(msg):
    print("\033[1m"+colors.G+"[*]"+colors.W+"", msg)

def text(msg):
    print("\033[1;94m[?]\033[0m", msg)

dashboard()

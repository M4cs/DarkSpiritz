#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config import startup
from core import helper
from core import welcome
from core import showlist
from terminaltables import SingleTable
import os, configparser, time, sys, glob, socket
try:
    if sys.platform.startswith('linux'):
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

    os.system("clear")
    def checkdat():
        if os.path.exists("config/userdat.ini") == True:
            version = "2.0"
            config = configparser.ConfigParser()
            config.read("config/userdat.ini")
            config['DEFAULT']['VERSION'] = version
            now = time.strftime("%c")
            config['DEFAULT']['LASTRUN'] = now
            with open("config/userdat.ini", "w") as configfile:
                config.write(configfile)
            print(colors.BLUE + "         [" + time.strftime("%H:%M") + "] Loaded Configuration File" + colors.END)
        else:
            startup.createdat()

    checkdat()
    os.system("clear")
    sx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = '0.0.0.0'
    try:
        sx.connect(('8.8.8.8', 80))
        hostname = sx.getsockname()
        data = "%s" % (hostname[0])
        print(colors.BLUE + "\n      [" + time.strftime("%H:%M") + "] Connected to a network.\n      [" + time.strftime("%H:%M") + "] Local IP Address:", data + colors.END)
    except:
        print("Failed To Establish Connection")
    welcome.welcome()
    checkdat()

    def main():
        print("")
        config = configparser.ConfigParser()
        config.read("config/userdat.ini")
        terminalname = colors.BLUE + "[" + colors.END + "DSPF" + colors.BLUE + "]> " + colors.END
        terminal = input(terminalname + colors.END)
        if terminal[0:4] == "help" or terminal == "?":
            helper.menu()
            main()
        elif terminal[0:5] == "clear":
            os.system("clear")
            welcome.welcome()
            main()
        elif terminal[0:] == "show":
            print(colors.GREEN)
            showlist.showlist()
            print(colors.END)
            main()
        elif terminal[0:3] == "use":
            if terminal[4:] == terminal[4:]:
                check = "%s.plugin" % (terminal[4:])
                if os.path.exists(check) == True:
                    os.system("%s.plugin" % (terminal[4:]))
                    main()
                else:
                    print(colors.RED + "[!]" + colors.END + "%s: Could Not Be Found!" % (terminal[4:]))
                    main()
        elif terminal[0:17] == "show " + terminal[5:]:
            print("")
            print(colors.BLUE + "Plugin Category: " + terminal[5:])
            print("==============")
            print("Name        ")
            print("" + colors.END)
            directorylist = glob.glob(terminal[5:] + "/*.plugin")
            for line in directorylist:
                about = line
                with open(about, "r") as myfile:
                    data = myfile.read().splitlines()
                    desc = data[0]
                    datar = desc.replace("Description = '", "")
                x = datar.rstrip("'")
                bb = line.split(terminal[5:] + "/")[1].split('.plugin')[0]
                print("{0:17s}".format(bb.upper()))
            print(" ")
            main()
        elif terminal[0:6] == "addkey":
            if terminal[7:] == terminal[7:]:
                print("")
                newkey = terminal[7:]
                newvalue = input("%s Value: " % (newkey))
                config['DEFAULT'][newkey] = newvalue
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                main()
        elif terminal[0:3] == "set":
            if terminal[4:] == "lhost":
                config['DEFAULT']['LHOST'] = input("\nEnter Value: ")
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                main()
            elif terminal[0:] == "set lport":
                config['DEFAULT']['LPORT'] = input("\nEnter Value: ")
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                main()
            elif terminal[4:9] == "rhost":
                config['DEFAULT']['RHOST'] = input("\nEnter Value: ")
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                main()
            elif terminal[4:9] == "rport":
                config['DEFAULT']['RPORT'] = input("\nEnter Value: ")
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                main()
            elif terminal[4:12] == "userlist":
                config['DEFAULT']['USERLIST'] = input("\nEnter Directory: ")
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                main()
            elif terminal[4:12] == "passlist":
                config['DEFAULT']['PASSLIST'] = input("\nEnter Directory: ")
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                main()
            elif terminal[4:13] == "interface":
                config['DEFAULT']['PASSLIST'] = input("\nEnter Interface: ")
                with open("config/userdat.ini", "w") as configfile:
                    config.write(configfile)
                main()
        elif terminal[0:5] == "reset":
            os.system("rm config/userdat.ini")
            startup.createdat()
            checkdat()
            main()
        elif terminal[0:4] == "exit":
            print("Exiting Framework..")
            exit()
        elif terminal[0:7] == "session":
            try:
                print(colors.GREEN)
                print("Key:              Value:")
                print("========================\n")
                for key, value in config.items('DEFAULT'):
                    pressed = "{0:17s}{1:12s}".format(key,value).upper()
                    print(pressed)
                print(colors.END)
                main()
            except KeyboardInterrupt:
                main()
        elif terminal[0:7] == "restart":
            os.system("./start.py")
        elif terminal[0:3] == "run":
            if terminal[4:] == terminal[4:]:
                os.system("%s" % (terminal[4:]))
                main()
        else:
            print("Unknown Command. Use help or ? to see available commands.")
            main()

    main()
except KeyboardInterrupt:
    main()

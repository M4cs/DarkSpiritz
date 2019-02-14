# -*- coding: utf-8 -*-
import sys
import configparser
import requests


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

def welcome():
    config = configparser.ConfigParser()
    config.read("config/userdat.ini")
    welcometext = colors.BLUE + """
      ██████╗   ███████╗  ██████╗   ███████╗
      ██╔══██╗  ██╔════╝  ██╔══██╗  ██╔════╝
      ██║  ██║  ███████╗  ██████╔╝  █████╗
      ██║  ██║  ╚════██║  ██╔═══╝   ██╔══╝
      ██████╔╝  ███████║  ██║       ██║
      ╚═════╝   ╚══════╝  ╚═╝       ╚═╝
      Dark  Spiritz  Penetesting  Framework
              Current Version: 2.0

     """ + colors.BLUE + """ Developed by Syntel - @syndicatedintel
           https://syndicatedintel.com/

     Use help or ? to see available commands.

For support open an issue on GitHub or E-Mail Us here:
           syndicatedintel@protonmail.com
""" + colors.END
    print(welcometext)

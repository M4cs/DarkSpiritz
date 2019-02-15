# -*- coding: utf-8 -*-
from terminaltables import SingleTable
import sys

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

def menu():
    table_data = [
        ['Command', 'Descriptions'],
        ['help or ?', 'Display this menu'],
        ['set <value>', 'Set a value in your loaded configuration'],
        ['addkey <key>', 'Add a custom key to your config. May be needed in some plugins.'],
        ['show', 'Show plugin categories'],
        ['show <category>', 'Show plugins inside that category'],
        ['info <category/plugin>', 'Show description of plugin'],
        ['use <category/plugin>', 'Use plugin inside a certain category'],
        ['reset', 'Set all values in your loaded configuration'],
        ['session', 'Show current configuration'],
        ['clear', 'Clear terminal screen'],
        ['run', 'Run a bash command'],
        ['restart', 'Restart Framework']
    ]
    table = SingleTable(table_data)
    header = colors.BLUE + """
Configurations:

Your current session will autosave any changes to the config you make.

You can add keys to your configuration by running the addkey command.

Plugins:

Some plugins may only work on certain platforms. If you would like to check
before running a plugin use the info command below. The developer of the
plugin will provide more info on what systems the plugin runs successfully
on.

Commands are CaSe SeNsItIvE
    """ + colors.END
    print(header)
    print(colors.BLUE + table.table + colors.END)

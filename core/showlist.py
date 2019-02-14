# -*- coding: utf-8 -*-
import glob

def showlist():
        print("""
Categories:
===========
""")
        for d in glob.iglob('*'):
    	       if "LICENSE" not in d:
                    if "README.md" not in d:
                        if "config" not in d:
                            if "core" not in d:
                                if "install" not in d:
                                    if "storage" not in d:
                                        if "CODE_OF_CONDUCT.md" not in d:
                                            if "modules" not in d:
                                                if "start.py" not in d:
                                                    if "requirements.txt" not in d:
                                                        print("""%s""" % (d.upper()))

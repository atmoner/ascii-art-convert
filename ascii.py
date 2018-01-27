# importing the requests library
from __future__ import print_function 
from binascii import *
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

# More fonts: http://www.figlet.org/examples.html
user_input = raw_input("Text: ")  
cprint(figlet_format(user_input, font="larry3d"),"blue")
 

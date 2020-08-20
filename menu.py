#!/usr/bin/env python3 

import subprocess
from inspect import getfullargspec
x = input("What can I do for you?")
programs = ["gedit","firefox", "vscode" , "terminator"]
counter = 0
def runprog():
    subprocess.call(prog)
    counter = counter  + 1
    
if ( ("start" in x) or ("run" in x) or ("execute" in x) ):
    for prog in programs: 

        if (prog in x):
            runprog()
        elif("terminal" in x):
            subprocess.call("gnome-terminal")
        elif("vscode" in x ):
            runprog("code")

    if(counter != 0 ):
        print("can't handle request")
args = getfullargspec(runprog)
print("number of arguments are ", len(args.args))



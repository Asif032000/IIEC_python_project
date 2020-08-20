#!/usr/bin/env python3 
import subprocess,os
print("HELLO THERE!")
os.system("""
    echo "Installing espeak ..." 
    espeak " To work properly we need to install espeak in the system " 
    sudo apt-get install espeak 
    clear
    espeak " May I know your name please ? " 
    read -p " Your name : " name
    espeak "Welcome $name. What can i do for you ? " 
""")
while True: 
    
    
    print("Please wait...")
    
    os.system("sleep 2")
    os.system("clear")
    x = input("What can I do for you?")
        
    if ( ("start" in x) or ("run" in x) or ("execute" in x) or ("open" in x )):
        # firefox
        if ("firefox" in x ) and ( ( "don't" not in x ) or ( "not" not in x ) ): 
            os.system("""
                espeak "Opening firefox .. please wait... ? " 
            """)
            z = os.system("firefox")
            if (int(z) != 0):
                os.system("""
                    espeak "it seems firefox isn't installed. Please install it first."
                """)
        
        #terminal
        elif("terminal" in x) and ( ("don't" not in x ) or ( "not" not in x ) ):
            os.system("""
                espeak "opening terminal .... "
            """)
            z = os.system("gnome-terminal")
            if (int(z) != 0):
                os.system("""
                    espeak "it seems terminal isn't installed. Please install it first." 
                """)

        #vscode
        elif("vscode" in x ) and ( ("don't" not in x ) or ( "not" not in x )) :
            os.system("""
                espeak "Opening Visual Studio Code .... Please Wait ... " 
            """)
            z = os.system("code")
            if (int(z) != 0):
                os.system("""
                    espeak "It seems Visual Studio Code isn't installed. Install it first" 
                """)
        #chrome
        elif("chrome" in x ) and ( ("don't" not in x ) or ( "not" not in x )) :
            os.system("""
                espeak "Opening chrome .... Please Wait ... " 
            """)
            z = os.system("google-chrome")
            if (int(z) != 0):
                os.system("""
                    espeak "It seems Chrome isn't installed. Install it first"
                """)

        #terminator
        elif("terminator" in x ) and ( ("don't" not in x ) or ( "not" not in x )) :
            os.system("""
                espeak "Opening terminator .... Please Wait ... " 
            """)
            z = os.system("terminator")
            if (int(z) != 0):
                os.system("""
                    espeak "It seems Terminator isn't installed. Install it first"
                """)
        
        #paint
        elif("paint" in x ) and ( ("don't" not in x ) or ( "not" not in x )) :
            os.system("""
                espeak "Opening Paint .... Please Wait ... " 
            """)
            z = os.system("mypaint")
            if (int(z) != 0):
                os.system("""
                    espeak "It seems Paint isn't installed. Install it first"
                """)
            
        #sudoku
        elif("sudoku" in x ) and ( ("don't" not in x ) or ( "not" not in x )) :
            
            os.system("""
                espeak "Starting Sudoku .... Please Wait ... " 
            """)
            z = os.system("sudoku")
            if (int(z) != 0):
                os.system("""
                    espeak "It seems Sudoku isn't installed. Install it first"
                """)
        #whatsapp
        elif("whatsapp" in x ) and ( ("don't" not in x ) or ( "not" not in x )) :
            os.system("""
                espeak "Opening Whatsapp .... Please Wait ... " 
            """)
            z = os.system("firefox https://web.whatsapp.com")
            if (int(z) != 0):
                os.system("""
                    espeak "Some error has occured . Please check your internet connection and install firefox"
                """)
            
        # notepad
        elif( ("notepad" in x ) or ( "text editor" in x ) or ("gedit" in x ) ) and ( ("don't" not in x ) or ( "not" not in x )) :
            os.system("""
                espeak "Opening Text Editor  .... Please Wait ... " 
            """)
            z = os.system("gedit")
            if (int(z) != 0):
                os.system("""
                    espeak "Gedit isn't installed . Please install it first."
                """)
        # ssh 
        elif( ("ssh" in x ) or ( "text editor" in x ) or ("gedit" in x ) ) and ( ("don't" not in x ) or ( "not" not in x )) :
            os.system("""
                espeak "Opening S S H service .... Please Wait ... "
                echo " Please Wait ... "
                sleep 2
                 
            """)
            z = os.system("""
            espeak "Enter the username and I Pe. address and follow the instructions..."
            read -p "Enter the username and IP address (username IP): " user IP
            ssh $user@$IP
            """)
            if (int(z) != 0):
                os.system("""
                    espeak "There. is. some error"
                """)
            
        

        else:
            os.system("""
            espeak "Sorry , I don't know how to do that." 
            espeak " Press Enter to continue" 
            """)
            print("can't handle request")
        input("To continue, Press ENTER!")
    elif("install" in x ) and ( ("don't" not in x ) or ( "not" not in x )) :
            os.system("""
                espeak " Enter the program name " 
            """)
            z = os.system("""
            read -p 'Please enter program name to install:' program
            sudo apt-get install $program
            """)
            if  (int(z) != 0 ):
                os.system("""
                    clearr
                    espeak " Can't install the program "
                    echo " Can't install the program "  
                """)
            else: 
                os.system("""
                    espeak "Installed successfully" 
                """)
    
    elif("exit" in x ) or ("quit" in x) or ("close" in x ) and ( ("don't" not in x ) or ( "not" not in x )) :
        break 
    else:
        os.system("""
            espeak "Sorry , I don't know how to do that." 
            espeak " Press Enter to continue" 
            """)
        print("can't handle request")
        input("To continue, Press ENTER!")
    
    



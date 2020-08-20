import os
import pyttsx3

while True:
    
    pyttsx3.speak("Hey Zeeshan how can i help you ")
    print("Hey Zeeshan how can i help you :",end='')
    p=input()
        
    if(("run" in p) or ("execute" in p)) and (("chrome" in p) or ("googlechrome" in p)):
        os.system("chrome") 
        pyttsx3.speak("chrome is executed")        
        
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and (("notepad" in p) or ("text editor" in p)):
        os.system("notepad")
        pyttsx3.speak("notepad is executed")   
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and ("firefox" in p):
        os.system("firefox")
        pyttsx3.speak("firefox is executed")
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and ("skype" in p):
        os.system("skype")
        pyttsx3.speak("skype is executed")        
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and ("calculator" in p):
        os.system("Calculator")
        pyttsx3.speak("calculator is executed")        
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and ("msedge" in p):
        os.system("msedge")
        pyttsx3.speak("Microsoft edge is executed")        
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and (("video player" in p) or ("vlc" in p)):
        os.system("vlc")
        pyttsx3.speak("video player is executed")    
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and (("virtual box" in p) or ("vmbox" in p)):
        os.system("VirtualBox")
        pyttsx3.speak("virtual box is executed")       
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and ("internet" in p):
        os.system("Internet Explorer")
        pyttsx3.speak("Internet explorer is executed") 
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and ("camera" in p):
        os.system("camera")
        pyttsx3.speak("camera is executed")    
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and (("cmd" in p) or ("command" in p) or ("command prompt" in p)):
        os.system("cmd")
        pyttsx3.speak("command prompt is executed") 
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and ("calendar" in p):
        os.system("calendar")
        pyttsx3.speak("calendar is executed") 
    
    elif(("run" in p) or ("execute" in p) or ("start" in p)) and (("wmplayer" in p) or ("media player" in p)):
        os.system("wmplayer")
        pyttsx3.speak("media player is executed")     
        
    elif(("exit" in p) or ("quit" in p) or ("stop" in p) or ("donot" in p) or ("don't" in p) or ("close" in p)):
        break

    else:
        print("either not present or path missing \n")
        pyttsx3.speak("Sorry,either software is not present or path missing..you can follow the link for help")
        print("TIP:-> if you installed the software and still unable to run,follow this link : https://www.computerhope.com/issues/ch000549.htm#:~:text=Setting%20the%20path%20and%20variables%20in%20Windows%20Vista,and%20click%20the%20Edit%20button.%20Add%20...%20 \n")
        print("                                 THANKYOU! Have a Good Day                         ")
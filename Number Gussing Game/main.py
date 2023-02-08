import random
import pyttsx3
import voice


while(True):
    print("Welcome To Number Gussing Game ")
    voice.welcome()
    print("1.To Play")
    print("2.Exit")
    choise = int(input("Choise:"))
    if(choise == 1):
        g_no = random.randrange(1,100)
        voice.number()
        no = int(input("\nEnter Your Number in (1-100):"))
        count = 0
        w = 7
        while(count<=6):
            if(g_no==no):
                print("\n\"{} is Write Gusse\" WINNER..!!!".format(g_no))
                print("Note:You have Gussed this number after {} gusses\n".format(count))
                speak = pyttsx3.init()
                speak.say(g_no)
                speak.say(' is Write Gusse WINNER')
                speak.runAndWait()
                break
            elif(no>100 or no<0):
                voice.no_()
            elif (g_no<no):
                speak = pyttsx3.init()
                speak.say(no)
                speak.say('is Greater')
                print('your Number {} is Greater '.format(no))
                speak.runAndWait()
            elif(g_no>no):
                speak = pyttsx3.init()
                speak.say(no)
                speak.say('is Lesser')
                print('your Number {} is Lesser '.format(no))
                speak.runAndWait()

            w-=1
            if(w==0):
                break

            speak = pyttsx3.init()
            speak.say('Remaning Gusses are')
            speak.say(w)
            print("Remaning Gusses:",w)
            speak.runAndWait()
            
            print("\nTry again(1-100):")
            voice.try_()
            no = int(input(""))

            count += 1

        if(w==0):
            speak = pyttsx3.init()
            speak.say('Oooohhhh you have to many wrong gusses')
            print("\"Oohh you have to many wrong gusses\" LOSSER.")
            speak.say('Corret Number is')
            speak.say(g_no)
            print('Corret Number :{}\n'.format(g_no))
            speak.runAndWait()
    elif(choise==2):
        voice.exit()
        break
    else:
        voice.invalid()  
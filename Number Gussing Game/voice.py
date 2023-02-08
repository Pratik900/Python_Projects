import pyttsx3

speak = pyttsx3.init()
v = speak.getProperty('voices')
rate = speak.getProperty('rate')
speak.setProperty('rate', rate+5)
speak.setProperty('voice', v[1].id)
speak.runAndWait()

def welcome():
   speak = pyttsx3.init()
   speak.say('Welcome To Number Gussing Game')
   speak.say('Chose 1 to play or 2 for exit')
   speak.runAndWait()

def number():
   speak = pyttsx3.init()
   speak.say('Enter Your Number in between 1 to 100')
   speak.runAndWait()

def no_():
   speak = pyttsx3.init()
   speak.say('Please enter number in between 1 to 100')
   print("Please enter number between (1-100)")
   speak.runAndWait()

def try_():
   speak = pyttsx3.init()
   speak.say('try again between 1 to 100')
   speak.runAndWait()

def exit():
   speak = pyttsx3.init()
   speak.say('Thanks For playing the game')
   print("Thanks For playing the game")
   speak.runAndWait()

def invalid():
   speak = pyttsx3.init()
   speak.say('Pleaase Enter Valid Input')
   print("Invalid Input")
   speak.runAndWait()  



if __name__ == "__main__":
   welcome()
   number()
   no_()
   try_()
   exit()
   invalid()
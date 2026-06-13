import datetime
def time_check():
 current_time = datetime.datetime.now()

 
 display_time = current_time.strftime("%H:%M:%S")
 print(f"The Time is {display_time}")
        


import webbrowser
def google():
 webbrowser.open("https://www.google.com")
 print("The Browser Opened Successfully")



import webbrowser
def open_youtube():
 webbrowser.open("https://www.youtube.com")
 print("Youtube Opened Successfully")



import random
def tell_jokes():
 jokes = ["I am An comedian hahaha",
         "You are a dumbass hehehe",
         "You are bald hohoho"]
 selected_joke = random.choice(jokes)
 print(selected_joke)


def greet():
 print("WELCOME BOSS")

def main():
 while True:
  print("\n========Jarvis V1 Welcomes You ")
  print("1. WHAT IS THE TIME")
  print("2. OPEN GOOGLE")
  print("3. OPEN YOUTUBE") 
  print("4. TELL ME A JOKE")
  print("5. EXIT")

  choice = input("Select your Options : ")
  if choice == "1":
   time_check()
  elif choice == "2":
   google()
  elif choice == "3":
   open_youtube()
  elif choice == "4":
   tell_jokes()
  elif choice == "5":
   print("EXITING JARVIS THANK YOU")
   break
  else:
   print("INVALID OPTIONS")
 


greet()
main()

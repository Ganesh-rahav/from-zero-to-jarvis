
print("\n =====Jarvis V1 at your Service=====")
print("Welcome Luffy")
while True :
    command = input("Want Should I Do  :")

    if command == "Hello":
                print("Jarvis1 : Hii How can i help you today")
    elif command == "Time":
        import datetime
        current_time = datetime.datetime.now()
        display_time = current_time.strftime("%H:%M:%S")
        print(f"The Time is {display_time}")

    elif command == "open google":
        import webbrowser
            
        webbrowser.open("https://www.google.com")
        print("Jarvis1 :The Browser Opened Successfully")
    elif command == "open youtube":
          
          import webbrowser
          webbrowser.open("https://www.youtube.com")
          print("Jarvis1 :Youtube Opened Successfully")

    elif command == "Tell Joke":
         import random

         jokes = ["Jarvis1 :I am An comedian hahaha",
                  "Jarvis1 :You are a dumbass hehehe",
                  "Jarvis1 :You are bald hohoho"]
         selected_joke = random.choice(jokes)
         print(selected_joke)
    elif command == "Bye":
         print("BOII Luffy ")
         break
    
    
    else :
     print("This Function is still under process")
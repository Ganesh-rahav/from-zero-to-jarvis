
logs =[
        "Failed Login",
        "Failed Login",
        "User Login",
        "Malware Detected",
        "User Logout"
    ]
def view_logs():
    print("\n====Logs Storage======")
    count = 1
    for log in logs:
        print(f"{count}.{log}")
        count += 1

def search_log():
    search_term = input("Enter Search Term: ")
    matches = 0
    for log in logs:
        
     if search_term in log:
            print(log)
            matches += 1
        
        
    if matches == 0:
            print ("no matches found")

        
    else:
            print(f"Total Matches: {matches}")
       
            
def Failed_login_counter():
     print("\n======Total Failed Logins Count========")
     count = 0
     for log in logs:
          
          if log == "Failed Login":
               count += 1
     else:
          print(f"Total failed login : {count}")

def malware_counter():
     print("\n =====Tolal Malware Count====")
     count = 0
     for log in logs:
          
          
          if log == "Malware Detected":
           count += 1
     else:
          print(f"Total Malware Detected : {count}")



def Report():
    Failed_login_count = 0
    user_login_count = 0
    Malware_Detected_count = 0
    User_Logout_count = 0
    count = 1
    for log in logs:
      if log == "Failed Login":
         
         Failed_login_count += 1
      elif log == "User Login":
         user_login_count += 1  
      elif log == "Malware Detected":
          Malware_Detected_count += 1
      else:
          User_Logout_count +=1 
        
          print("\n ======= Network Report ======")
          print(f"Total logs: {len(logs)}")
          print(f"Failed Logins:{Failed_login_count}")
          print(f"user Logins:{user_login_count}")
          print(f"Malware Alerts:{Malware_Detected_count}")
          print(f"User Logouts:{ User_Logout_count}")

def remove_logs():
  
   print("\n ===== Loga Lists ======")
   password = list(logs)

   count = 1

   for log in logs:
      print(f"{count}. {log}")
      count += 1
    
   choice = int(input("\nDelete Logs: "))

   

   if 1 <= choice <= len(log):
      removed_log = logs.pop(choice - 1 )
      
      print(f"{removed_log} removed successfully")
   else:
      print("Log Not Found")

def main():
    while True:
        print("\n ======Security Log Dashboard======")
        print("1. View Logs")
        print("2. Log Searcher")
        print("3. Failed Login Counter")
        print("4. Malware counter")
        print("5. Report")
        print("6. Log Remover")
        print("7. exit")

        choice = input("Sselect Your Options : ")

        if choice == "1":
            view_logs()
        elif choice == "2":
            search_log()
        elif choice == "3":
            Failed_login_counter()
        elif choice == "4":
            malware_counter()
        elif choice == "5":
            Report()
        elif choice == "6":
            remove_logs()
        elif choice == "7":
            print("Exiting Log Dashboard........")
            break
        else:
            print("Invalid Options .......") 
         
   
     

def login():
 correct_username = "luffy"
 correct_password = "Mugichan1"
 for i in range(3):
  print(f"\n Attempt {i + 1}")
  username = input("Enter your Username : " )
  password = input("Enter your Password :" )

  if username == correct_username and password == correct_password:
         print("Access Granted")
         return True
         
 else:
         print("Invalid Credentials")
         print(f"Attempt left {2 - i}")
         return False
 


if login():
   main()
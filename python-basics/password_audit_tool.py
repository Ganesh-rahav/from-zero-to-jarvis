passwords =[]

def add_Password():
 for i in range(3):
  add_password = input("Enter New Password:")
  passwords.append(add_password)

  print("Password added successfully !")

def view_password():
 
   print("\n==== Passwords======")
   count = 1
   
   for password in passwords:
    print(f"{count}. {password}")
    count += 1

def audit_password():
  print("\n======Passwo Audit=====")
  
  
  for password in passwords:
    has_upper = False
    has_lower = False
    has_digit = False
    

    for char in password:
     if char.isupper():
      has_upper = True
      
     elif char.islower():
      has_lower = True
     elif char.isdigit():
      has_digit = True



    

     if len(password) < 8:
      
      stre = "Weak"
     
     elif has_upper and has_lower and has_digit:
      
      stre = "Strong"
     
     else:
      
      stre = "Medium"

    print(f"{password} -> {stre}")


def report():
   Strong_Password = 0
   Medium_Password = 0
   Weak_Password = 0
   for password in passwords:
      
      has_lower = False
      has_upper = False
      has_digit = False

      for char in password:

        if char.islower():
          has_lower = True

        elif char.isupper():
          has_upper = True

        elif char.isdigit():
          has_digit = True


      if len(password) < 8:
         
         Weak_Password += 1
      elif has_upper and has_lower and has_digit:
         Strong_Password += 1
      else:
        Medium_Password += 1 

   print("\n===== SECURITY REPORT =====")

   print(f"Total Passwords: {len(passwords)}")
   print(f"Strong Passwords: {Strong_Password}")
   print(f"Medium Passwords: {Medium_Password}")
   print(f"Weak Passwords: {Weak_Password}")

def remove_password():
  
   print("\n ===== Current Passwords ======")
   password = list(passwords)

   count = 1

   for password in passwords:
      print(f"{count}. {password}")
      count += 1
    
   choice = int(input("\nDelete Passwords: "))

   

   if 1 <= choice <= len(passwords):
      removed_password = passwords.pop(choice - 1 )
      
      print(f"{removed_password} removed successfully")
   else:
      print("Password Not Found")
def main():
  while True:
    print("\n======Password_Audit_Tool_Dashboard=========")
    print("1. Add Password")
    print("2. View Password")
    print("3. Audit Password")
    print("4. Report")
    print("5. Remove Password")
    print("6. Exit")

    choice = input("Select Your Options : ")

    if choice == "1":
     add_Password()
    elif choice == "2":
     view_password()
    elif choice == "3": 
     audit_password()
    elif choice == "4":
      report()  
    elif choice == "5":
      remove_password()
    elif choice == "6":
      print("Exiting Dashboard...........")
      break
    else :
      print("Invalid Options====.")


main()






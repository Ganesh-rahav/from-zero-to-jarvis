def greet():
   print("Welcome SOC MASTER")

def port():
   print("=====Available Services in this Network======")
   ports = {
      21 : "FTP",
      22 : "SSH",
      25 : "SMTP",
      80 : "HTTP",
      443: "HTTPS"
   }
   for port in ports:
       print(f"{port} -> {ports[port]}")

def user():
   users = {
      "admin": "Full Access",
      "analyst":"Limited Access",
      "guest":"Read Only"
   }
   username = input ("Enter your Username : "  )
   if username in users:
      print(f"{username} -> {users[username]}")

def security_report():
    
     
    alerts = {
      "1. Failed Logins" : "Medium",
      "2. Port Scan Detected" : "low",
      "3. Malware Alert" : "High",
      "4. Suspicious IP" : "Medium"
    }

    print("\n ===== SECURITY ALERTS ======")
    for security_report in alerts:
       print(f"{security_report} -> {alerts[security_report]}")

alerts1 = [
   "Failed login",
   "Port Scan Detected",
   "Malware Alert"
]

def view_alerts():
   print("\n==== Security Alerts======")
   count = 1
   
   
   for alert in alerts1:
      print(f"{count}. {alert}")
      count += 1

def add_alerts():
 new_alert = input("Enter New Alert:")
 alerts1.append(new_alert)

 print("alert added successfully !")

def delete_alerts():
   
   print("\n ===== Current Alerts ======")
   count = 1

   for alert in alerts1:
      print(f"{count}. {alert}")
      count += 1
    
   choice = int(input("\nDelete Old Alerts: "))
   

   if 1 <= choice <= len(alerts1):
      removed_alerts = alerts1.pop(choice - 1 )
      print(f"{removed_alerts} removed successfully")
   else:
      print("Alert Not Found")


   
def main(): 
 while True:
   
   print("\n ===== SOC DASHBOARD =======")
   print("1. View Alerts")
   print("2. Add Alerts")
   print("3. Check User Access")
   print("4. Greetings")
   print("5. Port Scanner")
   print("6. Security report")
   print("7. Delete Alerts")
   print("8. Exit")
   


   choices = input("Select Options : ")

   if choices == "1":
      view_alerts()
   elif choices == "2":
      add_alerts()
   elif choices == "3":
      user()
   elif choices == "4":
      greet()
   elif choices == "5":
      port()
   elif choices == "6":
      security_report()
   elif choices == "7":
      delete_alerts()      
   elif choices == "8":
      print("Exiting SOC Dashboard")
      break
   else:
      print("Invalid options")

    
      
      
def usernames():
    
    correct_username = "luffy"
    correct_password = "Mugiwara1"
  
    
    
    for i in range(3):
        
        print(f"\n Attempt {i + 1}")

        username = input("Enter your Name: ")
        password = input("Enter your Password: ")

        if username == correct_username and password == correct_password:
         print("Access Granted")
         return True
         
        

        else:
         print("Invalid Credentials")
         print(f"Attempt left {2 - i}")
    return False
        
if usernames():
   main()
   





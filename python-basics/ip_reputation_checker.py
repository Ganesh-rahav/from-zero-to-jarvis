bad_ips = {
    "192.168.1.10": "Malware C2",
    "45.33.32.156": "Brute Force",
    "10.0.0.5": "Suspicious Activity"
}

def view_threats():
    for bad_ip in bad_ips:
       print(f"{bad_ip} -> {bad_ips[bad_ip]}")

def check_ip():
    ip = input("Enter Your IP : ")
    if ip in bad_ips:
        print("IP Exits....")
        print(f"Status : Malicious")
        print(f"Reason : {bad_ips[ip]}")
    else:
        print("IP Do Not Exit/Data cleared")

def add_ip():
    
   print("=====ADD NEW IP======")
   new_ip = input("Add New IP : " )
   status = input("Reason : " )
   bad_ips[new_ip] = status
   print("Ip Added Successfully.....")

def Remove_ip():
     print("\n ===== Cureent Ip's ======")
     count = 1

     for ip in bad_ips:
       print(f"{count}. {ip}")
       count += 1
     ips = list(bad_ips.keys())
     choice = int(input("\nDelete Old IP's: "))
   

     if 1 <= choice <= len(bad_ips):
         removed_ip = bad_ips.pop(ips[choice])
         print(f"{removed_ip} removed successfully")
     else:
          print("Ip Not Found")

def threat_report():
    
    
    malware_c2_count = 0
    Brute_count = 0
    supicious_count = 0
    
    for ip in bad_ips:
    
      if bad_ips[ip] == "Malware C2":
         malware_c2_count += 1
      elif bad_ips[ip] == "Brute Force":
         Brute_count += 1  
      else:
         supicious_count += 1
       
        
    print("\n ======= Network Report ======")
    print(f"Total logs: {len(bad_ips)}")
    print(f"Malware C2:{malware_c2_count}")
    print(f"Brute Force:{Brute_count}")
    print(f"Suspicious Acitivity:{supicious_count}")

def main():
    while True:
        print("/n====IP Reutation Checker Dashboard======")
        print("1. View Threats")
        print("2. Chech IP & Threats")
        print("3. Add IP")
        print("4. Remove IP & threat")
        print("5. Report")
        print("6. Exit")

        choice = input("Select Your Options : ")
        if choice == "1":
            view_threats()
        elif choice == "2":
            check_ip()
        elif choice == "3":
            add_ip()
        elif choice == "4":
            Remove_ip()
        elif choice == "5":
            threat_report()
        elif choice == "6":
            print("Exiting Dashboard .......")
            break
        else :
            print("Invalid Options..")

main()







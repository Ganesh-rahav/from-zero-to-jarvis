device1 = {
  "PC-01": "Online",
  "Sever-01":"Online",
  "Printer-01": "Offline"
 }
def available_devices():

 print("====Available Devices =======")
 count = 1
 for devices in device1:
  print(f"{count} . {devices}")
  count += 1

def Add_Device():
   print("=====ADD NEW DEVICE======")
   new_device = input("Add New Devices : " )
   status = input("Status (online/offline): " )
   device1[new_device] = status

   print("Device Added Successfully")

def remove_device():
   print("\n ===== Current Devices ======")
   device = list(device1.keys())

   count = 1

   for devices in device1:
      print(f"{count}. {devices}")
      count += 1
    
   choice = int(input("\nDelete Old Devices: "))

   

   if 1 <= choice <= len(devices):
      removed_device = device[choice - 1 ]
      del device1[removed_device]
      print(f"{removed_device} removed successfully")
   else:
      print("Device Not Found")

def network():
   online_count = 0
   offline_count = 0
   for device in device1:
      if device1[device] == "Online":
         
         online_count += 1
      else:
         offline_count += 1
        
   print("\n ======= Network Report ======")
   print(f"Total Devices: {len(device1)}")
   print(f"Online Devices:{online_count}")
   print(f"Offline Devices:{offline_count}")

def check_device_status():

    print("\n===== DEVICE STATUS CHECK =====")

    device_name = input("Enter Device Name: ")

    if device_name in device1:

        print(f"{device_name} -> {device1[device_name]}")

    else:

        print("Device Not Found")

def main():
   while True:
      print("\n ===== Network Monitor =====")
      print("1. View Devices")
      print("2. Add Devices")
      print("3. remove Devices")
      print("4. Device Status")
      print("5. Reports")
      print("6. Exit")

      choice = input("Select Options: " )
      if choice == "1":
         available_devices()
      elif choice == "2":
         Add_Device()
      elif choice == "3":
         remove_device()
      elif choice == "4":
         check_device_status()
      elif choice == "5":
         network()
      elif choice == "6":
         print("Exiting Network Monitor.......")  
         break
      else:
         print("Invalid Options")

def login():
 correct_username = "Admin"
 correct_password = "Nono123"
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
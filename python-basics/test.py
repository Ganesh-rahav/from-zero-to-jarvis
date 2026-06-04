def login():

    correct_username = "admin"
    correct_password = "cyber123"

    for i in range(3):

        print(f"\nAttempt {i + 1}")

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == correct_username and password == correct_password:
            print("Access Granted")
            return True

        else:
            print("Invalid Credentials")
            print(f"Attempts Left: {2 - i}")

    return False
login()
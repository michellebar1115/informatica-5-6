import getpass

def main():

    password = int(150809)
    attempt = int(getpass.getpass(prompt = "What's the password? "))
    if attempt == password:
        print("Correct Password")

    print("Thank you!")

if __name__ == "__main__":
    main()

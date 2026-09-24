def main():

    numlist = [1,2,3,4,5,6,7,8,9,10]
    exit = 1
    
    while exit == 1:
        number = int(input("Enter a number (1-10): "))
        if number in numlist:
            print(f"Here is the {number} times table")

            for i in range(len(numlist)):
                times = number*(i+1)
                print(f"{i+1} times {number} is {times}")

            option = input("Would you like to exit? ").strip().lower()
            if option == "yes":
                exit -= 1
            else:
                 exit = 1
        else:
                print("Please provide a number 1-10")

if __name__ == "__main__":
    main()

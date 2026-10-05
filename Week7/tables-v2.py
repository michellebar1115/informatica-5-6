def main():
    numlist = [1,2,3,4,5,6,7,8,9,10]
    exit = 1
    print("Welcome to the times table quiz")
    validation = True



    while validation:
        try:
            number = int(input("Enter a number times table that you would like to be tested on: "))
            if number >= 1:
                if number <= 10:
                    validation = False
        except ValueError:
                    print("Invalid")

    validation_2 = True
    while validation_2:
        try:
            max_value = int(input("Enter the maximum value for your times table: "))
            validation_2 = False
        except ValueError:
            print("Invalid")


    if number in numlist:
        print(f"You will be tested on the {number} times table")

    for i in range(1, max_value+1):
        times = number*(i)
        validation_3 = True
        while validation_3:
            try:
                user_answer = int(input(f"{i} times {number}... "))
                validation_3 = False
            except ValueError:
                print("Invalid")

        if user_answer == times:
            print("Correct")
        else:
            print("Incorrect")



if __name__ == "__main__":
    main()

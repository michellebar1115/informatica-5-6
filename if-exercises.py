def main():

    print("Absolute Value Calculator")

    number = int(input("Write a number. "))

    if number < 0:
        print(number*-1)
    else:
        print(number)


    print("Input Calculator")

    number1 = float(input("Write a number. "))
    number2 = float(input("Write another number. "))
    operation = input("Type one operation: add, multiply, or subtract. ")

    if operation == "add":
        print(number1 + number2)
    elif operation == "multiply":
        print(number1 * number2)
    elif operation == "subtract":
        print(number1 - number2)
    else:
        print("ERROR, TRY AGAIN")


    print("Hard - String Calculator")

    eq = float((input("Write an arithmetic expression"))
    equation = eq.split( )
    operation = [1]
    number =  [0]
    number2 = [2]


if __name__ == "__main__":
    main()

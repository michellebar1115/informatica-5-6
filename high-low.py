def main():

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    highest(num1, num2)
    num3 = int(input("Enter a third number: "))
    lowest(num1,num2,num3)


def highest(a,b):
    if a > b:
        highest_num = a
    else:
        highest_num = b

    print(f"The highest number enteres is {highest_num}")


def lowest(a, b, c):
    if a<b and a<c:
        lowest_num = a
    elif b<a and b<c:
        lowest_num = b
    else:
        lowest_num = c

    print(f"The lowest number entered is {lowest_num}")


if __name__ == "__main__":
    main()

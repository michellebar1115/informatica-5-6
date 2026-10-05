def main():

    def calculate(a,b):
        answer = a + b
        print(f"{a} + {b} = {round(answer,1)}")

    num1 = 10
    num2 = 15

    calculate(num1, num2)

    def average_value(a,b,c):
        answer = (a + b + c) / 3
        print(f"The average value is {answer}")

    num3 = float(input("Enter first number: "))
    num4 = float(input("Enter second number: "))
    num5 = float(input("Enter fifth number: "))

    average_value(num3, num4, num5)

if __name__ == "__main__":
    main()

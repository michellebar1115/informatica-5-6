def main():
    print("Welcome!")
    print("Explanation:")


    valid_bits = ["0","1"]
    while True:
        user_binary_num = input("Enter a binary number: ")
        valid_chars = 0
        for user_bit in user_binary_num:
            if user_bit in valid_bits:
                valid_chars +=1
        if valid_chars == len(user_binary_num):
            break
        else:
            print("Invalid number.")
    binary_to_decimal(user_binary_num)

def binary_to_decimal(binary_num):
    decimal_num = 0
    for bit in binary_num:
        decimal_num = (decimal_num) * 2 + int(bit)
    print(decimal_num)

if __name__ == "__main__":
    main()

#my code
# def main():
#     def binary_to_decimal(binary_str)
#         try:
#             decimal_val = 0

#             for digit in binary_str
#                 decimal_val = decimal_val * 2 + int(digit)

#             print(f"Decimal number: {decimal_val}")

#         except ValueError:
#             print("Invalid binary number! Please enter only 0s and 1s")

#         print("Binary to Decimal Converter")
#         print("Explanation")

#         user_input= (input("Enter a binary number: ").strip()

#         binary_to_decimal(user_input)

# if __name__ == "__main__":
#     main()


def main():
    # #Read a file
    # with open("sample.txt") as new_file:
    #     content = new_file.read()
    #     print(content)

    # #Turn file content into a list
    # count = 0
    # with open("sample.txt") as hoco_week:
    #     for line in hoco_week:
    #         line = line.replace("\n","")
    #         count += 1
    #         print(f"Day {count}: {line}")

    # Assignment
    largest("numbers.txt")

def largest(file):
    number_list = []
    with open(file) as number_file:
        for number in number_file:
            number = number.replace("\n","")
            number_list.append(int(number))

    print(max(number_list))


if __name__ == "__main__":
    main()

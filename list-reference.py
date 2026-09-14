def main():

    pets = ["Dog","Cat","Hamster","Fish"]
    pets.append("Bird")
    pets.insert("Bunny")


    x = len("hello")

    print(x)
    password = [1, 2, 3, 4, 5, 6, 7, 8]
    xx = ["a", "b", "c", "d"]
    print(len(xx))
    print(password)
    change = input(" ")

    if change == "y":
        password[1]= 4
        password[0] = 2
        password[7] = 1
        password[6] = 9
        password[5] = 10
        print(password)

    numbers = [10, 2, 5, 3, 4, 8, 7]
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))

    tacos = ["Pastor", "Asada", "Suadero", "Rajas", "Papa", "Dorados", "Buche"]
    print(tacos)
    print(tacos.pop(3))
    print(tacos)


if __name__ == "__main__":
    main()


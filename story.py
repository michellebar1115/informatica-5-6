def main():
    # planet = input("Planet:")

    # # Separation
    # print("Hello",planet)

    # # Concatenation
    # print("Hello " + planet)

    # # Formatted Strings
    # print(f"Hello {planet}")

    # # Ending
    # print("Hello", end=" ")
    # print(planet)


    name = input("What is your name? ")
    color = input("Tell me a color: ")
    adj = input("Name a random adjective: ")
    goal = input("Goal you would like to achive: ")

    print(f"Hello, {name}!")
    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}")


if __name__ == "__main__":
    main()

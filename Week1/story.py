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


    name = input("What is your name? ").strip().title()
    color = input("Tell me a color: ").strip().lower()
    adj = input("Name a random adjective: ").strip().lower()
    goal = input("Goal you would like to achive: ").strip().lower()

    print(f"Hello, {name}!")
    print()

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}")
    print()
    print("This is your story in uppercase:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}".upper())

if __name__ == "__main__":
    main()

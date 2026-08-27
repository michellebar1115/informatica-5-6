def main():

    atmosphere = input("Descent atmosphere layer: ").strip().title()

    if atmosphere == "Exosphere":
        print("Your altitude level will be between 700 to 10,000 km")
    elif atmosphere == "Thermosphere":
        print("Your altitude level will be between 85 to 700 km")
    elif atmosphere == "Mesosphere":
        print("Your altitude level will be between 50 to 85 km")
    elif atmosphere == "Stratosphere":
        print("Your altitude level will be between 12 to 50 km")
    elif atmosphere == "Troposphere":
        print("Your altitude level will be between 0 to 12 km")
    else:
        print("Invalid answer. Try again.")

    starting = int(input("Enter exact altitud"))
    starting *= 1000
    starting /= 

    print("Total descent time:", starting)

if __name__ == "__main__":
    main()

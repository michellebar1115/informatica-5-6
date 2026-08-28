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
        print("Invalid answer.")


    starting = float(input("Enter exact altitud").strip())
    starting *= 1000

    if atmosphere == "Exosphere":
        starting /= 2000
        eq = round(starting + ((700000-85000)/500) + ((85000-50000)/200) + ((50000-12000)/75) + (12000/20),1)
        print("Total descent time:",eq)
    elif atmosphere == "Thermosphere":
        starting /= 500
        eq = round(starting ((85000-50000)/200) + ((50000-12000)/75) + (12000/20),1)
        print("Total descent time:",eq)
    elif atmosphere == "Mesosphere":
        starting /= 200
        eq = round(starting + ((50000-12000)/75) + (12000/20),1)
        print("Total descent time:",eq)
    elif atmosphere == "Stratosphere":
        starting /= 75
        eq = round(starting + (12000/20),1)
        print("Total descent time:",eq)
    elif atmosphere == "Troposphere":
        starting /= round(20,1)
        print("Total descent time:",starting)
    else:
        print("Non-valid number. Try again.")

if __name__ == "__main__":
    main()

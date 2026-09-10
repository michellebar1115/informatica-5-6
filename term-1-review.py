from datetime import datetime
def main():

    day = datetime.now().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print (days[day])

    if day < 4:
        print("It's a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("It's Friday")
        print("Just a day left until the weekend")
    else:
        print("It's the weekend!")

    months = ["January","February", "March", "April", "May", "June", "July", "August", "October", "November", "December"]
    seasons = ["Winter", "Spring", "Summer", "Autumn"]
    month = datetime.now().month
    print("It is", months[month-1])

    if month <= 2 or month == 12:
        season = 0
    elif month <= 5:
        season = 1
    elif month <= 8:
        season = 2
    else:
        season = 3

    print("It is", seasons[season])


if __name__ == "__main__":
    main()

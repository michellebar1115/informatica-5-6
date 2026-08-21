def main():
    transitors= 17800000000
    years = int(input("Years for the time into the future: "))

    transitors*= 2**(years/2)
    print("It'll have this many transitors:",transitors)
if __name__ == "__main__":
    main()


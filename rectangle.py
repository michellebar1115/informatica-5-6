def main():

    w = int(input("Enter width: "))

    print("O"*w)
    print("O"*w)
    print("O"*w)
    print("O"*w)
    print("O"*w)

    perm = 3+3+w+w
    area = 5*w
    print("Perimeter:",perm)
    print("Area:",area)

    #d = 5**2 + w**2
    #d2= (d)/.5
    #print(d2)

if __name__ == "__main__":
    main()

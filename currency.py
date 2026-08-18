def main():

    pesosc=float(input("How many pesos do you have? "))
    soles=float(input("How many soles do you have? "))
    reais=float(input("How many reais do you have? "))

    pesosctu= pesosc*0.00032
    solestu= soles*0.3
    reaistu= reais*0.19

    total=pesosctu+solestu+reaistu
    total=round(total,2)
    print("Total in USD:",total)

    pesosctp= pesosc*0.0054
    solestp= soles*5.07
    reaistp= reais*3.27

    total2=pesosctp+solestp+reaistp
    total2=round(total2,2)
    print("Total in pesos:",total2)


if __name__ == "__main__":
    main()

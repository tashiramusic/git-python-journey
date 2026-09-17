

def weight():
    weight = int(input("Enter your weight: "))
    unit = input("(L)bs or (K)g: ".lower())

    if unit == "l":
        converted = weight * 0.45
        print(converted)
    else:
        converted = weight /0.45
        print(converted)

weight()
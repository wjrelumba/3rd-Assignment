def amoApple():
    amoAppleF = int(input("Enter amount of apple/s: "))
    return amoAppleF

def amoOrange():
    amoOrangeF = int(input("Enter the amount of orange/s: "))
    return amoOrangeF

def price(appleF, orangeF, applePrF, orangePrF):
    priceVal = (appleF*applePrF) + (orangeF*orangePrF)
    return priceVal

def displaying(priceValF):
    print(f"The total amount is {priceValF}.")


apple = amoApple()
orange = amoOrange()
applePr = 20
orangePr = 25
priceVal = price(apple, orange, applePr, orangePr)
displaying(priceVal)
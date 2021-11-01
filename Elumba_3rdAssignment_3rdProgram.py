def moneyInput():
    amountMoney = int(input("Enter the amount of money you have: "))
    return amountMoney

def applePrice():
    applePr = int(input("Enter the price of apple: "))
    return applePr

def numApple(moneyF, applePrF):
    appleNum = moneyF // applePrF
    return appleNum

def moneyChange(moneyF, applePrF):
    changeF = moneyF % applePrF
    return changeF

def displayOutput(amo_appleF, changeF):
    print(f"You can buy {amo_appleF} apples and your change is {changeF} pesos.")

money = moneyInput()
applePr = applePrice()
amo_apple = numApple(money, applePr)
change = moneyChange(money, applePr)
displayOutput(amo_apple, change)
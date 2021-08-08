userInput = int(input("Please input an integer to test if it is prime. "))
if userInput <= -1:
    print("As the topic of negative prime numbers is still being debated today, I will not currently include them. Please try again later. ")
    exit()

def checkPrimeValidity():
    x = userInput
    y = x
    validityList = 0
    while y > 0:
        x=userInput%y
        if x==0:
            validityList += 1
        y -= 1

    if validityList == 2:
        print("This number is prime.")
    else:
        print("This number is not prime.")


checkPrimeValidity()
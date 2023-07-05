
def getAge(age):
    cat = "baby"
    if (age <= 5):
        cat = "baby"
    elif (age >5 and age<=13):
        cat = "kids"
    else:
        cat = "big people"
    return cat


myage = input("enter your age as an integer (ex. 5)")
print(getAge(int(myage)))

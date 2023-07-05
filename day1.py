print("hello world")

age = 53
pi = 3.14
name = "Mark"
iscool = True
print (age+pi)
print(age / pi)
print(age * pi)
niceoutput = round(age * pi,1)
print("your name is" + name + "and your age is" + str(age))


myage = input("what is your age")
if(myage > 50):
    print("you are old")
elif(int(myage) <=19 and int(myage)>=13):
    print("your a teen")
else:
    print("you are old")

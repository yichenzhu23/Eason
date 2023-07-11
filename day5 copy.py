 
def getKidz(data):
    # the math numsurv / numkids * 100
    numkids = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[6] != ""): # error check for missing data
            if (float(temp[6]) < 16.0):
                numkids = numkids + 1
                if (temp[1] == "1"):
                    numsurv = numsurv + 1
    return (numsurv / numkids) * 100

def getGrp(data,sex):
    # the math numsurv / numgrp * 100
    numgrp = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[5] == sex):
            numgrp = numgrp + 1
            if (temp[1] == "1"):
                numsurv = numsurv + 1
    return (numsurv / numgrp) * 100      
# open our titanic database
file = open("titanic.csv","r") # r is read only
cols = file.readline() # gets first line of data
data = file.readlines()
file.close()

fo = open("indexl.html","w")
fo.write("<html>")
fo.write("<h1>Women and Children First?</h1>")
fo.write("</html>")
fo.write("<br>")
fo.write("<h2>Study conclusion</h2>")
fo.write("<svg width='800' height='500'>")
fo.write("<rect width='740' height='100'fill='#ff0303'></rect>")
fo.write("<text x='25' y='25' fill='white'>Women</text>")
fo.write("<rect y='125'width='590' height='100' fill='green'></rect>")
fo.write("<rect y='250' width='190' height='100' fill='yellow' </rect>")
fo.write("</svg>")
fo.write("</html>")

fo.close()





# create 'game loop' using while

keepgoing = True
while (keepgoing == True):
    key = input("w for female, k for kids, m for men, q for quit")
    if (key == "q"):
        keepgoing = False
        print("bye")
    elif (key == "w"):
        result = getGrp(data,"female") # send result to variable
        print(round(result,1))
    elif (key == "m"):
        result = getGrp(data,"male")
        print(round(result,1))
    elif (key == "k"):
        result = getKidz(data)
        print(round(result,1))
    else:
        print("umm follow instructions please")




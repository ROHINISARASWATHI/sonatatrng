def highestnum(no1,no2=5,no3=15):
    if(no1>no2) and (no1>no3):
       return no1

    elif(no2>no3):
       return no2

    else:
       return no3
var = highestnum(2,5,15)
print(var,"is highest")
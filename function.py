def add(no1,no2=10,no3=300):
    sum = no1+no2
    return sum

result = add(10,10)
print(result)
result = add(10.6,10.7)
print(result)
result = add("sonata","software")
print(result)
result = add(True,False)
print(result)

result = add([1,2,3,4],[10])
print (result)
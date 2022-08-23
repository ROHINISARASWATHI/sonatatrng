p1=input()
p2=input()
if (p1==p2):
    print("its a tie")
elif (p1=="rock" and p2=="scissor"):
    print(" p1 wins")
elif (p1=="paper" and p2=="rock"):
    print("p1 wins")
elif (p1=="scissor" and p2=="paper"):
    print("p1 wins")
else :
    print("p2 wins")

def rockpaperscissor (p1,p2):
    if (p1==p2):
        return p1,p2
    elif (p1=="rock" and p2=="scissor"):
        return p1
    elif (p1=="paper" and p2=="rock"):
        return p1
    elif (p1=="scissor" and p2=="paper"):
        return p1
    else:
        return p2


var = rockpaperscissor ("rock","paper")
print(var,"wins")

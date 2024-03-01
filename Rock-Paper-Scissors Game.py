#Rock Paper Scissor game
P="P"
R="R"
S="S"
x,y=input().split()
if x==P and y==P or x==R and y==R or x==S and y==S:
    print("D")
elif x==P and y==R or x==R and y==P:
     print("P")
elif x==R and y==S or x==S and y==R:
     print("R")
else:
    print("S")

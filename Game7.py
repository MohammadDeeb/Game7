# !/usr/bin/python3
player = 1
summation = 0
x = 0
print("Welcome To 100Game")
while 1:
    if player == 1:
        print("Player 1 it's your turn")
        x = int(input())
        if 11 > x > 0:
            summation += x
            player = 2
        else:
            print("Please Choose Between 1 to 10")
        print("Summation = ",summation)
    if summation >= 100:
        print("Player 1 Is The Winner")
        break
    elif player == 2:
        print("Player 2 it's your turn")
        x = int(input())
        if 11 > x > 0:
            summation += x
            player = 1
        else:
            print("Please Choose Between 1 to 10")
        print("Summation = ", summation)
        if summation >= 100:
            print("Player 2 Is The Winner")
            break


import random
num = random.randint(1,100)
x=0
while True:
    print("Guess a number between 1 and 100")
    guess = input()
    i = int(guess)
    if i == num:
        print ("You guessed right!")
        x=x+1
        break
    elif i < num:
        print("Try higher")
        x=x+1
    elif i> num:
        print ("Try lower")
        x=x+1
numb = random.randint(1,100)
b=0
while True:
    print("Guess a number between 1 and 100")
    gues = input()
    i = int(gues)
    if i == numb:
        print ("You guessed right!")
        b=b+1
        break
    elif i < numb:
        print("Try higher")
        b=b+1
    elif i> numb:
        print ("Try lower")
        b=b+1
if num == numb:
    print("Tie!")
elif x > b:
    print("Player 2 wins!")
elif x < b:
    print("Player 1 wins!")

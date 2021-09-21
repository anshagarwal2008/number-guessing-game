import random
print("guessing game")
number=random.randint(1,9)
chances=0

while chances<5:
    guess=int(input("guess a number between 1-9 "))
    if guess==number:
        print("Congratulaion You Won")
    chances+=1
if not chances < 5:
    print("You Lose !! the number is",number)
import random

print("Hi! wellcome to the number guessing game.\n You have 7 Changes to guess the nunber let's start!")

low = int(input("Enter the lower bound :"))

high  = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low,high)

ch=7

gc=0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))
    
    if guess == num:
        print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")
        
        break
    
    elif guess > num:
        print("Too high! Try a lower numer")
    
    elif guess < num:
        print("Too low! Try a higher number.")

        
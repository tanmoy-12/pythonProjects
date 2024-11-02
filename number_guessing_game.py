#Dice Rolling Game Implementation
import random

while(1):
    choice=input("Play the game? (y/n): ").lower()
    if(choice=='y'):
        random_number=random.randint(1,100)
        try:
            n=int(input("Enter a random number between 1 & 100 : "))
            if(n<1 or n>100):
                print("Invalid input")
            elif(random_number<n):
                print("Too high!")
            elif(random_number>n):
                print("Too low!")
            elif(random_number==n):
                print("Congratulations! You guessed correctly.")
            else:
                print("Sorry! Better luck next time")
        except ValueError:
            print("Invalid input")
    elif(choice=='n'):
        print("Thanks For Playing!")
        break
    else:
        print("Invalid choice. Please enter y or n.")

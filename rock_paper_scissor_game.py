import random

choices=('r', 'p', 's')

while True:
    choice=input("Enter your choice(r/p/s/n): ").lower()
    if(choice in choices):
        computer_choice=random.choice(choices)
        print("Computer chosen", computer_choice, "You choosen", choice)
        if(choice==computer_choice):
            print("It's a tie!")
        elif((choice=='r' and computer_choice=='s') or 
            (choice=='p' and computer_choice=='r') or 
            (choice=='s' and computer_choice=='p')):
            print("You win!")
        else:
            print("Computer wins!")
    elif(choice=="n"):
        print("Thanks For Playing")
    else:
        print("Invalid choice. Please enter r, p, s or n.")
        break
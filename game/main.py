'''
    Created on September 15, 2021
    @author joeypy
'''
'''
Requirement:
 1. Show the number range form 1 to 100
 2. Game should ask us to guess a number
 3. Give a clue of the number is higher or lower than the guess
 4. Inform the player if he won
'''

from random import randint

start = 1
end = 100
value = randint(start, end)
guess = None
counter = 1

print(f"The computer choice between {start} and {end}")

while True:
    try:
        guess = int(input("Is your turn, choose a number in that range: "))
        if guess == value:
            print("That's the number, you won! 🥳🎉👏")
            print(f"Attemps: {counter} 😜")
            break
        elif guess < value:
            print("To lower 📉")
            counter += 1
        else:
            print("To Higher 📈")
            counter += 1
    except TypeError as e:
        print("You must enter a correct value.", e)
    except ValueError as e:
        print("You must enter a correct value.", e)

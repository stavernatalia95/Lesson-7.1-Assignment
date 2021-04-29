import random
number = random.randrange(0, 50,3)

game_condition = input("I am thinking of a number between 0 and 50.")
number_of_guesses = 0
print('You only have 7 chances to guess the integer. Please take a guess:')

while number_of_guesses < 7:
    user_guess = int(input())
    number_of_guesses += 1
    if user_guess < number:
        print('The value is too low')
    if user_guess > number:
        print('The value is too high')
    if user_guess == number:
        break
if user_guess == number:
    print('You guessed correctly')
else:
    print('You did not guess the number. Try next time!')
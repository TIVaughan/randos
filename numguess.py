import random

number = random.randint(1,99)

player_name = input("What yo name?: ")

print('Alrighty there ' + player_name + ', I am guessing a number between 1 and 99. You get 5 tries: ')

number_of_guesses = 0

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number you big dummy, The number was ' + str(number))
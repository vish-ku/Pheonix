import random
print('Guess a number between 1 and 20')
secretnumber = random.randint(1,20)
for i in range(1,7):
    print('Take a Guess.')
    guess = input()
    if guess < secretnumber:
        print('Your guess is  low.')
    elif guess > secretnumber:
        print('Your guess is high')
    else:
        break
if guess == secretnumber:
    print('You have the correct Guess, Congrats.')
    print('It took you ' + str(i)+' tries to make the correct guess.')
else:
    print('Better luck next time.')

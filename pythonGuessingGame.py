# Here we are setting some variables, the variables with value "" are left empty as values will be added later.
# We are setting a guess limit for the letter_guess section and the phrase_guess sections of this application.
secret_phrase = ("I love Python")
letter_guess = ""
store_letter = ""
letter_guess_count = 0
letter_guess_limit = 8
phrase_guess = ""
phrase_guess_count = 0
phrase_guess_limit = 3

# Here we are setting a while loop that will run 8 times. The if statement will see if the later_guess is found in the secret_phrase.
# If the letter_guess is in the secret_phrase it will be added to the empty store_letter variable.
# IF the letter_guess is not found in the secret_phrase no value will be added to the store_letter variable.
# In both cases the value x is given to the letter_guess counter and 1 is added each time a guess is made, with the number of guesses left being printed.
while letter_guess_count < letter_guess_limit:
    letter_guess = input("Try and guess a letter! :")
    if letter_guess in secret_phrase:
        print("Yes!")
        store_letter += letter_guess
        letter_guess_count += 1
        x = letter_guess_count
        print("Guesses left:", 8- x)
        
    if letter_guess not in secret_phrase:
        print("Nope!")
        letter_guess_count += 1
        x = letter_guess_count
        print("Guesses left:", 8 - x)

print("\n")
print("Now it's time to guess the phrase!")

# This part finds the length of the store_letter variable as an int is needed. If the value is greater or equal to one it prints a different message.
if len(store_letter) >= 1:
    print("\nWell done, you guessed", len(store_letter), "correctly!")
    print("These letters are found in the secret phrase!", store_letter)
else:
    print("\nUnfortunatly you didn't guess any letters correctly, you can still try and guess the phrase!")

print("\nYou have three tries to guess the phrase!")

# This part determines what happens when phrase guesses are made. 
# As long as the guess and the phrase aren't the same and the phrase_guess_count is smaller than the phrase_guess_limit, the loop will run. 
# The else statement will run when the phrase_guess_count becomes bigger than the phrase_guess_limit and break the loop.
# The break is needed otherwise only the loop will keep running and since its the only condition being met it will continue to print. 
# If however the phrase_guess is the same as the secret_phrase, the if statement will run and the game will end.
while phrase_guess != secret_phrase:
    if phrase_guess_count < phrase_guess_limit:
        phrase_guess = input("Enter guess: ")
        phrase_guess_count += 1
        x = phrase_guess_count
        print("Guesses left:", 3 - x)
    else:
        print("You didn't guess the phrase, you loose!")
        break

if phrase_guess == secret_phrase:
    print("Well done, you got it! The phrase was \"I love Python\"!")
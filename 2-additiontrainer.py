# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

from random import randrange
title = "** A Simple Addition Quiz **"
print("*" * len(title))
print(title)
print("*" * len(title))

player = input("Please enter your name here: ")

print(f"Welcome to the quiz, {player}!")
print("What are we waiting for? Let's start the quiz!")

MaxScore = 10
CurrentScore = 0

count = 1
while count <= 10:
    addend1 = randrange(0, 99)
    addend2 = randrange(0, 99)
    sum = addend1 + addend2
    print(f"Question #{count}")
    print(f"{str(addend1)} + {str(addend2)}")
    answer = int(input("Your answer: "))
    if int(answer) == sum:
        CurrentScore += 1
        print("Your answer is correct!")
    else:
        print(f"Your answer is incorrect! The right answer is {sum}.")
    count = count + 1
print(f"You got {CurrentScore} out of {MaxScore} questions correct.")
if CurrentScore == 10:
    print(f"Congratulations, {player}! You have mastered adding numbers!")
elif CurrentScore >= 6 and CurrentScore <= 9:
    print(f"You did great, {player}! Study more and you'll ace this quiz soon!")
else:
    if CurrentScore <= 5:
        print(f"You failed the quiz, {player}! Try to focus on this lesson first.")
        print("Better luck next time!")

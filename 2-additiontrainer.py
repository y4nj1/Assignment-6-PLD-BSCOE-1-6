# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

from random import randrange
import time
print("\n")
title = "** A Simple Addition Quiz **"
print("*" * len(title))
print(title)
print("*" * len(title))

print("\n")

player = input("\33[1m\033[33mPlease enter your name here: \033[0m")

print("\n")

print("-" * 24)

print(f"\33[31m\33[1mWelcome to the quiz,\033[0m \33[1m\33[3m\033[33m{player}!\033[0m")
print("\n")
print("\33[1mWhat are we waiting for? Let's start the quiz!\033[0m")

print("-" * 24)
print("\n")

title = "** A Simple Addition Quiz **"
print("*" * len(title))
print(title)
print("*" * len(title))
print("\n")
MaxScore = 10
CurrentScore = 0
tic = time.perf_counter()
count = 1
while count <= 10:
    addend1 = randrange(0, 99)
    addend2 = randrange(0, 99)
    sum = addend1 + addend2
    print(f"\33[1m\33[3mQuestion #{count}\33[0m")
    print(f"\33[1m\33[94m{str(addend1)}\33[0m + \33[1m\33[95m{str(addend2)}\33[0m")
    answer = int(input("\33[32mYour answer:\33[0m"))
    if int(answer) == sum:
        CurrentScore += 1
        print("\33[1m\33[92mYour answer is correct!\33[0m")
        print("\n")
    else:
        print(f"\33[1m\33[91mYour answer is incorrect! The right answer is\33[0m \33[1m\33[93m{sum}.\33[0m")
        print("\n")
    count = count + 1
toc = time.perf_counter()

print("-" * 24)
print("\n")

print(f"\33[1mYou have taken the quiz in\33[0m \33[95m\33[1m\33[3m{toc - tic:0.2f}\33[0m \33[1mseconds.\33[0m")
print(f"\33[1m\33[3mYou got \33[32m\33[1m{CurrentScore}\33[0m \33[1m\33[3mout of\33[0m \33[34m\33[1m{MaxScore}\33[0m \33[1m\33[3mquestions correct.\33[0m")
if CurrentScore == 10:
    print(f"\33[92m\33[1mCongratulations,\033[0m \33[1m\33[3m\033[33m{player}!\033[0m \33[92m\33[1mYou have mastered adding numbers!\033[0m ")
elif CurrentScore >= 6 and CurrentScore <= 9:
    print(f"\33[94m\33[1mYou did great,\033[0m \33[1m\33[3m\033[33m{player}!\033[0m! \33[94m\33[1mStudy more and you'll ace this quiz soon!\033[0m ")
else:
    if CurrentScore <= 5:
        print(f"\33[1m\33[91mYou failed the quiz,\033[0m \33[1m\33[3m\033[33m{player}!\033[0m \33[1m\33[91mTry to focus on this lesson first.\033[0m")
        print("\33[1mBetter luck next time!\033[0m")
print("\n")
print("-" * 24)
print("\n")
print("\33[1m\33[35mThank you for taking this quiz.\033[0m")
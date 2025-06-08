# Python mplementation of 'CracklePop' by iris
# For Recurse Center Application, June 2025
# 
# Prompt:
# Write a program that prints out the numbers 1 to 100 
# (inclusive). If the number is divisible by 3, print 
# Crackle instead of the number. If it's divisible by 5, 
# print Pop instead of the number. If it's divisible by 
# both 3 and 5, print CracklePop instead of the number. 
# You can use any language.

for number in range(1,101):
    divisibleBy3 = number % 3 == 0
    divisibleBy5 = number % 5 == 0

    if (divisibleBy3 and divisibleBy5):
        print("CracklePop")
    elif (divisibleBy3):
        print("Crackle")
    elif (divisibleBy5):
        print("Pop")
    else:
        print(number)
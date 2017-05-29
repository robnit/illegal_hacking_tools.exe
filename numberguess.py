# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:52:38 2017

@author: Linux
"""

high = 100
low = 0

print("Please think of a number between 0 and 100!")
while True == True:
    guess = int((high+low)/2)
    print("Is your secret number",guess,"?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
    answer = str(input(""))
    if answer == "h":
        high = guess
    elif answer == "l":
        low = guess
    elif answer == "c":
        break
    else:
        print("incorrect input")
        
print ("Game over. Your secret number was:", guess)
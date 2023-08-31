# In this project we will be running a program to determine the budget leftover after expenses 
# 8-28-2023
# CTI-110 P1HW2 - Travel Expense
# Ian Blanchard
#

print('This program calculates and displays trip expenses.')

print('In the following texts you are to answer a series', end='') 
print(' of questions.')

print()

print('What is your budget for this trip?')

budget = int(input())

print('Where will You be Traveling?')

travel = input()

print('How much will you spend on gas?')

gas = int(input())

print('Approximately, how much will you need for room/board?')

board = int(input())

print('Lastly, how much money will you spend on food?')

food = int(input())

print('----------Travel Expenses----------')

print('Travel Location:', travel)
print('Initial Budget:', budget)
print('Fuel Expense:', gas)
print('Room & Board', board)
print('Food Expense:', food)


remaining = budget - gas - board - food 

print('Remaning Balance:', remaining)

print('Your remaining balance after expenses is', remaining)
print('Enjoy your trip to', travel)
'''
Filename : quiz_game.py
Author : Amit Maurya
'''

print("Welcome to Quiz Game!")

playing = input("Do you want to Play? ")

if playing.lower() != "yes":
    print("See you next time . . . ")
    quit()
  
print("Starting the game play. . .")
name = input("What is your name? ")
score = 00
total = 40
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct")
    score += 10
else: 
    print("Wrong answer!")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct")
    score += 10
else: 
    print("Wrong answer!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct")
    score += 10
else: 
    print("Wrong answer!")

answer = input("What does PSU stand for? ")
if answer == "power supply unit":
    print("Correct")
    score += 10
else: 
    print("Wrong answer!")
    
print(f"Hi {name}, Your Score is {score}/{total}.")
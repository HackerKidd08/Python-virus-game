import os
import console

def level1():
    console.clear()
    print("Since this is level 1 i will go easy on you.\nMake a Hello, World! program, for the string use single quotes or '' use print('') and then put your text in the quoates:\n")
    lvl1code = input("")
    if lvl1code == "print('Hello, World!')":
        print("Correct")
        console.startConsole(True)
    else:
        print("Try again and check your syntax")
        level1()

def level2():
    print("Make a string variable and once again use single quotes AKA ''\nalso the name should be myString and the text in the variable quotes should be 'This is a string!'")
    Level2Code = input("")
    if Level2Code == "myString = 'This is a string!'":
        print("Correct")
    else:
        print("Try again and check your syntax")
import os
import console

prompt = ">>> "


def level1():
    console.clear()
    print("Since this is level 1 i will go easy on you.\nMake a Hello, World! program, for the string use single quotes or '' use print('') and then put your text in the quotes:\n")
    Level1Code = input(prompt)
    if Level1Code == "print('Hello, World!')":
        console.successMessage("Correct!")
        console.userLevel = 2
        console.startConsole(True)
    else:
        console.errorMessage("Try again and check your syntax")
        level1()

def level2():
    print("Make a string variable and once again use single quotes AKA ''\nalso the name should be myString and the text in the variable quotes should be 'This is a string!'")
    Level2Code = input(prompt)
    if Level2Code == "myString = 'This is a string!'":
        console.successMessage("Correct!")
        console.increaseLevel()
    else:
        console.errorMessage("Try again and check your syntax")
        level2()
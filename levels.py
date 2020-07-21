import os
import console
import time

prompt = ">>> "


def level1():
    console.clear()
    print("Since this is level 1 i will go easy on you.\nMake a Hello, World! program, for the string use single quotes or '' use print('') and then put your text in the quotes:\n")
    Level1Code = input(prompt)
    if Level1Code == "print('Hello, World!')":
        console.successMessage("Correct!")
        console.userLevel = 2
        time.sleep(1)
        console.startConsole(True)
    else:
        console.errorMessage("Try again and check your syntax")
        time.sleep(0.5)   
        level1()

def level2():
    print("Make a string variable and once again use single quotes AKA ''\nalso the name should be myString and the text in the variable quotes should be 'This is a string!'")
    Level2Code = input(prompt)
    if Level2Code == "myString = 'This is a string!'":
        console.successMessage("Correct!")
        time.sleep(1)
        console.userLevel = 3
        console.startConsole(True)
    else:
        console.errorMessage("Try again and check your syntax")
        time.sleep(0.5)
        level2()

def level3():
    print("Time to combine the code from level 1 and level 2 this time type print(myString)")
    Level3Code = input(prompt)
    if Level3Code == 'print(myString)':
        print('This is a string!')
        console.userLevel = 4
        console.successMessage("Correct!")
    

def level4(partNum):
    if partNum == 1:
        print("Welcome to level 4 in this level we are going to work on 2 more variable types! In this level we are going to focus on INTEGERS and FLOATS.")
        print("A INTEGER is a whole number while a FLOAT is a number with a decimal at the end.")
        print("First you will make a INTEGER variable. type myInt = 5")
        Level4CodePart1 = input(prompt)
        if Level4CodePart1 == "myInt = 5":
            console.successMessage("Congrats! time for floats")
            time.sleep(1)
            console.clear()
            level4(2)
        else:
            console.errorMessage("Wrong! please try again and check your syntax")
            time.sleep(1)
            console.clear()
            level4(1)
    if partNum == 2:
        print("To make a float type myFloat = 5.0 notice the decimal point? without the decimal point the variable would just be a integer")
        Level4CodePart2 = input(prompt)
        if Level4CodePart2 == "myFloat = 5.0":
            console.successMessage("Congrats!")
            level4(3)
            time.sleep(1)
            console.clear()
        else:
            console.errorMessage("Wrong! please try again and check your syntax")
            time.sleep(1)
            console.clear()
            level4(2)
    if partNum == 3:
       print("Make a int(Short for integer) variable called damage and give it a value of 5")
       Level4CodePart3 = input(prompt)
       if Level4CodePart3  == "damage = 5":
           console.successMessage("So the virus was at 100 hp when you started this level.")
           console.successMessage("Im going to send back you the console in 5 seconds and i need you to type virusHealth")
           time.sleep(5)
           console.clear()
           console.damageVirus(5)
           console.userLevel = 5
       else:
           console.errorMessage("Wrong! please check your syntax and try again")

    def level5():
        print("Level 5")
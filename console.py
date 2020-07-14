import os
import levels
import colorama
import json

colorama.init()

userLevel=1

def clear():
    import platform
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def successMessage(*args):
    print(colorama.Fore.GREEN + ' '.join(args) + colorama.Style.RESET_ALL)

def errorMessage(*args):
    print(colorama.Fore.RED + ' '.join(args) + colorama.Style.RESET_ALL)

def startConsole(helpUnlocked):
    commands = json.load(open('commands.json'))

    clear()
    level = userLevel
    while True:
        command = input("root@ROOT-PC:~ ")

        if command == "help":
            if helpUnlocked == False:
                errorMessage("ERROR HELP UNAVAILABLE PLEASE TYPE PLAY TO UNLOCK")
            else:
                for cmd in commands:
                    print(commands[cmd]["usage"])
        elif command == "play":
            levels.playLevel(userLevel)
        elif command == "clear":
            clear()
        elif command == "quit":
            exit()
        else:
            errorMessage("Unknown command:", command)

def increaseLevel():
    global userLevel
    userLevel += 1
    print(str(userLevel))
    userLevel += 1

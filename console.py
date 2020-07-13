import os
import levels
import colorama

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
    commands = {'clear':'clear -- clears the console',
    'play':'play -- use play to get closer to the end of the game and unlock more commands'}

    clear()
    level = userLevel
    while True:
        command = input("root@ROOT-PC:~ ")
        if command == "help":
            if helpUnlocked == False:
                errorMessage("ERROR HELP UNAVAILABLE PLEASE TYPE PLAY TO UNLOCK")
            else:
                for command in commands.keys():
                    print(commands[command])
        elif command == "play":
            if level == 1:
                levels.level1()
        elif command == "clear":
            clear()
        elif command == "quit":
            exit()

def increaseLevel():
    global userLevel
    userLevel += 1
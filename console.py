import os
import levels

userLevel=1

def clear():
    import platform
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def startConsole(helpUnlocked):
    commands = {'clear':'clear -- clears the console','play':'play -- use play to get closer to the end of the game and unlock more commands'}
    clear()
    level = userLevel
    while True:
        command = input("root@ROOT-PC:~ ")
        if command == "help":
            if helpUnlocked == False:
                print("ERROR HELP UNAVAILABLE PLEASE TYPE PLAY TO UNLOCK")
                helpUnlocked = True
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
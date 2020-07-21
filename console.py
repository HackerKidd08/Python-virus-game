import os
import levels
import colorama
import json
import saveManager

colorama.init()

userLevel=1
virusHealth=100

def damageVirus(damageAmnt):
    global virusHealth
    virusHealth -= damageAmnt

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
    print(userLevel)
    while True:
        if virusHealth == 0:
            print("CONGRATS YOU BEAT THE VIRUS!1!1!!!!11!")

        command = input("root@ROOT-PC:~ ")
        

        if command == "help":
            if helpUnlocked == False:
                errorMessage("ERROR HELP UNAVAILABLE PLEASE TYPE 'play' TO UNLOCK")
            else:
                for cmd in commands:
                    print(commands[cmd]["usage"])
        elif command == "play":
            if level == 1:
                levels.level1()
            elif level == 2:
                levels.level2()
            elif level == 3:
                levels.level3()
            elif level == 4:
                levels.level4(1)
            else:
                print(f"Stop cheating bro! That's not your cup of tea! There's no level {level}")
        elif command == "clear":
            clear()
        elif command == "quit":
            exit()
        elif command == "save":
            saveManager.saveGame()
        elif command == "virushealth":
            print(str(virusHealth))
        else:
            errorMessage("Unknown command:", command)

def increaseLevel():
    global userLevel
    userLevel += 1
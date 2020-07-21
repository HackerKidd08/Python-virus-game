import os
import levels
import colorama
import json
import saveManager

colorama.init()

userLevel=1
virusHealth=100

debugMode = False

def damageVirus(damageAmnt):
    global virusHealth
    virusHealth -= damageAmnt

def clear():
    import platform
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def printMessage(*args, color):
    print(color + ' '.join([str(arg) for arg in args]) + colorama.Style.RESET_ALL)

def successMessage(*args):
    printMessage(*args, color=colorama.Fore.GREEN)

def errorMessage(*args):
    printMessage(*args, color=colorama.Fore.RED)

def helpMessage(*args):
    printMessage(*args, color=colorama.Fore.BLUE)
    

def startConsole(helpUnlocked):
    global debugMode
    global userLevel

    commands = json.load(open('commands.json'))

    clear()
    level = userLevel
    print(userLevel)
    while True:
        if virusHealth == 0:
            print("CONGRATS YOU BEAT THE VIRUS!1!1!!!!11!")

        text = input("root@ROOT-PC:~ ")
        command = text.split()[0]
        args = text.split()[1:]

        if command == "help":
            if helpUnlocked == False:
                errorMessage("ERROR HELP UNAVAILABLE PLEASE TYPE 'play' TO UNLOCK")
            else:
                for cmd in commands:
                    helpMessage(commands[cmd]["usage"])
        elif command == "play":
            if level == 1:
                levels.level1()
            elif level == 2:
                levels.level2()
            elif level == 3:
                levels.level3()
            elif level == 4:
                print('Level 4 bro finally!')
                levels.level4(1)
            else:
                print(f"Stop cheating bro! That's not your cup of tea! There's no level {level}")
        elif command == "clear":
            clear()
        elif command == "quit":
            saveManager.saveGame()
            exit()
        elif command == "save":
            saveManager.saveGame()
        elif command == "virushealth":
            print(virusHealth)
        elif command == "__DEBUG__":
            if not debugMode:  
                print("Great! Do you think you are smart? Guess this little genius!")
                password = input("Password: ")

                if not password == "hw!Wr7$@BCR8":
                    errorMessage("Sike! That's the wrong password! Not as smart as I tought!")
                    continue

                successMessage("How?!?!?!!! I guess you are a really smart person!")
                debugMode = True
                continue

            debug_commands = {"load": "load -- Loads the save.json file",
                              "setlevel": "setlevel -- Sets your current level"}

            if len(args) == 0:
                for cmd in debug_commands:
                    helpMessage(debug_commands[cmd])
            elif len(args) == 1:
                if args[0] == "load":
                    saveManager.loadGame()
            elif len(args) == 2:
                if args[0] == "setlevel":
                    print(args)
                    if not args[1].isnumeric():
                        continue
                    level = int(args[1])
                    userLevel = level
                    successMessage("User level updated", userLevel)
                    
        else:
            errorMessage("Unknown command:", command)

def increaseLevel():
    global userLevel
    userLevel += 1
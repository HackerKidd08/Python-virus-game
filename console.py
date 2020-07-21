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

def successMessage(*args):
    print(colorama.Fore.GREEN + ' '.join(args) + colorama.Style.RESET_ALL)

def errorMessage(*args):
    print(colorama.Fore.RED + ' '.join(args) + colorama.Style.RESET_ALL)

def startConsole(helpUnlocked):
    global userLevel
    global debugMode
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
                    print(commands[cmd]["usage"])
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

            if len(args) == 0:
                errorMessage("Sike! That's the wrong number of arguments")
            elif len(args) == 1:
                if args[0] == "load":
                    saveManager.loadGame()
                elif args[0] == "setlevel":
                    if not args[1].isnumeric():
                        continue
                    userLevel = int(args[1])
                    successMessage("User level updated", userLevel)
                    
        else:
            errorMessage("Unknown command:", command)

def increaseLevel():
    global userLevel
    userLevel += 1
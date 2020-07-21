import json
import console

savePath = "save.json"
save = json.load(open(savePath))

def saveGame():
    save["userLevel"] = console.userLevel
    save["virusHealth"] = console.virusHealth
    with open(savePath, 'w') as f:
        f.write(json.dumps(save))

    print("Saved", save)

def loadGame():
    console.userLevel = save["userLevel"]
    console.virusHealth = save["virusHealth"]
    print("Loaded last save", save)

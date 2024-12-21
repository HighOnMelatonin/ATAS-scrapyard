#hahaha
import json

def openJson(filename) -> dict:
    ## Open json file, return dictionary
    file = open(filename)
    users = json.load(file)
    return users

def createUser(userID):
    ## Creates a new user
    return None

def changePoints(newPoints):
    ## Add or subtract points form the user, return None
    return None

def commitJson():
    ## Open json file, dump into json, return None
    return None

def getPoints() -> int:
    ## get points of an item
    return None

def main():
    ## Main loop
    return None

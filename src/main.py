#hahaha
import json

def openJson(filename) -> dict:
    ## Open json file, return dictionary
    file = open(filename, 'r+')
    users = json.load(file)
    file.close()
    return users

def createUser(userID):
    ## Creates a new user
    return None

def changePoints(newPoints):
    ## Add or subtract points form the user, return None
    return None

def commitJson(users, filename):
    ## Open json file, dump into json, return None
    """
    users is a dict of user IDs with their associated points

    filename is the filepath for the json file

    return val: None
    """
    file = open(filename, 'r+')
    json.dumps(users, file)
    file.close()
    return None

def getPoints() -> int:
    ## get points of an item
    return None

def main():
    ## Main loop
    return None

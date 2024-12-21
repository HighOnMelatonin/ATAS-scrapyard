#hahaha
import json

def openJson(filename) -> dict:
    ## Open json file with file path of <filename>, return dictionary
    file = open(filename, 'r+')
    users = json.load(file)
    file.close()
    return users

def createUser(userID, users):
    ## Creates a new user (if does not exist), return None
    if userID not in users.keys():
        users[userID] = 0
    return None

def changePoints(newPoints, userID, users):
    ## Add or subtract points form the user, return None
    users[userID] += newPoints
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

def getPoints(item, filename) -> int:
    ## Opens market dictionary, checks the appropriate points of the item, 
    # returns the points the item is worth
    ## Dictionary is in the format of { item : {"Qty": X, "Points": Y} }
    file = open(filename, 'r+')
    market = json.load(file)
    file.close()
    points=0
    if item not in market.keys():
        print("New Item! Please contact admin support.")
    else:
        points = market[item]["Points"]
    return points

def main():
    ## Main loop
    return None

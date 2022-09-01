
# Your code here
import random

def chat():
    coworkers = ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee = coworkers[random.randint(0,3)]
    print("Chatting with " + chatee + "...")
    print("Done")

def getWater():
    print("Getting water...")
    print("That was refreshing.")

def useSocialMedia():
    socialMedia = ["FaceBook", "Twitter", "YouTube", "Reddit"]
    choice = socialMedia[random.randint(0,3)]
    print("Using " + choice + "...")
    print("Done")
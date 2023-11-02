from home.chores import takeOutTrash, sweepFloors, doDishes
from home.cook import washVegetables, chopMeat
from home.leisure import playGames, petDog, readBook, takeNap

# from office.work import code, attendMeeting, updateSchedule
# from office.idle import chat, getWater, useSocialMedia
from office import code, attendMeeting, updateSchedule, chat, getWater, useSocialMedia



def morningMenu():
  print("Starting the day off...")
  while True:
    print(
      "\nWhat do you want to do? \n1: Take out trash\n2: Sweep the floor\n3: Go to work\n4: Quit"
    )
    choice = input("> ")
    if choice == "1":
      takeOutTrash()
    elif choice == "2":
      sweepFloors()
    elif choice == "3":
      print("Going to work...")
      workMenu()
      break
    elif choice == "4":
      print("Bye!")
      quit()
    else:
      print("Please enter a valid input")
    
  


def workMenu():
  while True:
    print(
      "\nWhat do you want to do? \n1: Code\n2: Attend meeting\n3: Update schedule\n4: Slack off\n5: Go Home\n6: Quit"
    )
    choice = input("> ")
    if choice == "1":
      code()
    elif choice == "2":
      attendMeeting()
    elif choice == "3":
      updateSchedule()
    elif choice == "4":
      slackOffMenu()
      break
    elif choice == "5":
      print("Going home...\n")
      eveningMenu()
      break
    elif choice == "6":
      print("Bye!")
      quit()
    else:
      print("Please enter a valid input")
  


def slackOffMenu():
  while True:
    print(
      "\nWhat do you want to do? \n1: Chat\n2: Get water\n3: Use social media\n4: Back to work\n5: Quit"
    )
    choice = input("> ")
    if choice == "1":
      chat()
    elif choice == "2":
      getWater()
    elif choice == "3":
      useSocialMedia()
    elif choice == "4":
      workMenu()
      break
    elif choice == "5":
      print("Bye!")
      quit()
    else:
      print("Please enter a valid input")
  


def eveningMenu():
  while True:
    print(
      "\nWhat do you want to do? \n1: Chores\n2: Leisure\n3: Sleep\n4: Quit"
    )
    choice = input("> ")
    if choice == "1":
      choresMenu()
    elif choice == "2":
      leisureMenu()
    elif choice == "3":
      print("Going to sleep...\n\n\n\n")
      print("Waking up the next morning...")
      morningMenu()
    elif choice == "4":
      print("Bye!")
      quit()
    else:
      print("Please enter a valid input")
  
def choresMenu():
  while True:
    print(
      "\nWhat do you want to do? \n1: Do dishes\n2: Wash vegetables\n3: Chop meat\n4: Return to evening menu\n5: Quit"
    )
    choice = input("> ")
    if choice == "1":
      doDishes()
    elif choice == "2":
      washVegetables()
    elif choice == "3":
      chopMeat()
    elif choice == "4":
      eveningMenu()
    elif choice == "5":
      print("Bye!")
      quit()
    else:
      print("Please enter a valid input")

def leisureMenu():
  while True:
    print(
      "\nWhat do you want to do? \n1: Play games\n2: Pet dog\n3: Read book\n4: Take nap\n5: Return to evening menu\n6: Quit"
    )
    choice = input("> ")
    if choice == "1":
      playGames()
    elif choice == "2":
      petDog()
    elif choice == "3":
      readBook()
    elif choice == "4":
      takeNap()
    elif choice == "5":
      eveningMenu()
    elif choice == "6":
      print("Bye!")
      quit()
    else:
      print("Please enter a valid input")

morningMenu()
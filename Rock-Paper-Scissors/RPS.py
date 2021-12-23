import random
import time
import dbStuff
options = ["rock","spock","paper","lizard","scissors"]


def gameMode():

    print("Gamemodes:")
    print("One game...   1")
    print("Best of 3...  3   //not finished")
    print("Best of 5...  5   //not finished")
    ans = input("choice: ")
    print(ans)
    if int(ans) == 1:
        print("Game starts.", end="", flush=True)
        time.sleep(0.25)
        print(".", end="", flush=True)
        time.sleep(0.25)
        print(".", end="", flush=True)
        time.sleep(1.25)
        print(".", end="", flush=True)
        print(".", end="", flush=True)
        time.sleep(0.25)
        print(".")
        print("")
        print("")
        print("")

def inputOfUser():
    print("____________________________________")
    print("rock, paper scissors, lizard, spock")
    print("____________________________________")
    print(" ")
    userInput = input("choice: ").lower()
    if userInput in options:
        #print("bugTest UserInput: ",userInput)                                     bug test
        return userInput
    else:
        exit()



def inputOfPC():
    inputPC = random.randint(0,4)
   # print("Test: InputPc ",inputPC)                                                bug test
    return inputPC

def convertAndGetAnswers(user,pc):
    numberToWord = {"rock":0,"paper":2,"scissors":4,"lizard":3,"spock":1}
    usernum = numberToWord.get(user)
    #print("BugTest-User: ",user,usernum)                                           bug test
    pcnum = pc
    return (usernum-pcnum) % 5


def getPCWord(pc):
    numberToWord = {"rock": 0, "paper": 2, "scissors": 4, "lizard": 3, "spock": 1}
    pcnum = pc
    pcWord=(list(numberToWord.keys())[list(numberToWord.values()).index((pcnum))])
    #print("Bug-Test-PC:",pcnum,pcWord)                                             bug test
    return pcWord

def getresult(erg):
    if erg == 0:
        result = "Draw"
    elif erg == 1 or erg == 2:
        result = "Victory"
    elif erg > 2:
        result = "Defeat"
    return result
def matchReport(userInput,pcinput,result):
    print("--------------------------------")
    print("Match Result:")
    print("You took:",userInput)
    print("Pc took:",getPCWord(pcinput))
    print("Match Status:",result)
    print("--------------------------------")

def summaryforDB(userinput,values):
    name = values[0]
    rock = values[1]
    paper = values[2]
    scissors = values[3]
    lizard = values[4]
    spock = values[5]
    if userinput == "rock":
        rock = rock+1
    elif userinput == "paper":
        paper = paper+1
    elif userinput == "scissors":
        scissors = scissors+1
    elif userinput == "lizard":
        lizard = lizard+1
    elif userinput == "spock":
        spock = spock+1
    newvalues = name,rock,paper,scissors,lizard,spock
    return newvalues


#gameMode()
userinput = inputOfUser()
pcinput = inputOfPC()
erg = convertAndGetAnswers(userinput,pcinput)
result = getresult(erg)
matchReport(userinput,pcinput,result)
if (result == "Victory"):
    dbStuff.connect()
    dbStuff.createTable()
    if(dbStuff.nocolums() == 0):
        dbStuff.firstInsert()
    values = dbStuff.selectValues()
    print(values)
    newvalues= summaryforDB(userinput,values)
    dbStuff.drop()
    dbStuff.createTable()
    print(newvalues)
    dbStuff.insert(newvalues)
exit()




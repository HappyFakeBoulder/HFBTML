# IMPORTANT NOTE:
# This program reads from myMachine.txt.
# Before running, edit myMachine.txt
# to hold the description you want.
# Note that the default starting card
# is card 1, so set card 1 to be a starting
# card.

from tm import *
def createCard(text):
	motionDict = {"L":-1, "R":1, "S":0}
	retDict = {}
	parsed = text.split("\n")
	for x in parsed:
		retDict[x[0]] = ProgramCardLine(x[1], motionDict[x[2]], int(x[3:]))
	return ProgramCard(retDict)
def createMachine(fileName):
	cardl = []
	mdescfile = open(fileName, "r")
	mdescr = mdescfile.read().split("\n----\n")
	mdescfile.close()
	for x in mdescr:
		cardl.append(createCard(x))
	return TuringMachine(cardl)
myMachine = createMachine("myMachine.txt")
myMachine.run(list(input("Pick a starting tape: ")), 1)

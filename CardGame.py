""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def showDeck():
  print "Location of All Cards\n"
  print "#\t card\t\tlocation"
  for x in range(len(cardLoc)):
    if len(cardLoc[x]) == 3:
      print str(x) + "\t" + rankName[int(cardLoc[x][1])] + " of " + suitName[int(cardLoc[x][0])] + "     " + playerName[int(cardLoc[x][2])]
    else:
      rank = int(cardLoc[x][1]+cardLoc[x][2])
      print str(x) + "\t" + rankName[rank] + " of "  + suitName[int(cardLoc[x][0])] + "     " + playerName[int(cardLoc[x][3])]
    

def clearDeck():
  c = 0
  for s in range(0, 4):
    for r in range(0, 13):
      cardLoc[c] = str(s) + str(r) + str(0)
      c+=1

        
def assignCard(player):
  ran_num = randrange(0, 52)
  modify_card = str(cardLoc[ran_num])
  while modify_card[-1] != "0":
    ran_num = randrange(0,52)
    modify_card = str(cardLoc[ran_num])
  new_card = modify_card[:-1] + str(player)
  cardLoc[ran_num] = new_card
    
def showHand(player):
  print "\n"
  if player == 1:
      print "Displaying Player's Hand:"
  else:
      print "Displaying Computer's Hand:"
  for x in range(len(cardLoc)):
    string_card = cardLoc[x]
    find_player = int(string_card[-1])
    
    if find_player == player:
      if len(cardLoc[x]) == 3:
        print rankName[int(cardLoc[x][1])] + " of " + suitName[int(cardLoc[x][0])]
      else:
        rank = int(cardLoc[x][1]+cardLoc[x][2])
        print rankName[rank] + " of "  + suitName[int(cardLoc[x][0])]
     
           
    
def main():
  clearDeck()
  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)
  ex = raw_input("")

main()


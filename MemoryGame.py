# import randint to decide which player plays 1
from random import randint
# Defining necessary Dictionary
player1Score=0
player2Score=0
listofPlayers=["Player1","Player2"]

# Showing Cards Dictonary from front
fromFront={"00":"[Father]",
"01":"[Tree]",
"02":"[Moon]",
"03":"[Cat]",
"04":"[Dog]",
"05":"[Sun]",
"06":"[Star]",
"07":"[Light]",
"08":"[Dark]",
"09":"[Mother]",
"10":"[Tree]",
"11":"[Moon]",
"12":"[Cat]",
"13":"[Dog]",
"14":"[Sun]",
"15":"[Star]",
"16":"[Light]",
"17":"[Dark]",
"18":"[Mother]",
"19":"[Father]"   
}


# Showing Cards Dictonary from back
fromBack={"00":"[****]",
"01":"[****]",
"02":"[****]",
"03":"[****]",
"04":"[****]",
"05":"[****]",
"06":"[****]",
"07":"[****]",
"08":"[****]",
"09":"[****]",
"10":"[****]",
"11":"[****]",
"12":"[****]",
"13":"[****]",
"14":"[****]",
"15":"[****]",
"16":"[****]",
"17":"[****]",
"18":"[****]",
"19":"[****]"   
}

# Cards Dictonary during gameplay
dictTemp = fromBack.copy()

class Card:
  def displayFirst(self):
    listDisplay=[]
    for key,value in dictTemp.items():
      s=str(key)+str(value)
      listDisplay.append(s)
      if len(listDisplay)==5:
        print(" ".join(listDisplay))
        listDisplay.clear()

  def deckShow(self):
    listDisplay=[]
    for key,value in fromFront.items():
      s=str(key)+str(value)
      listDisplay.append(s)
      if len(listDisplay)==5:
        print(" ".join(listDisplay))
        listDisplay.clear()

  def afterPlayShow(self,Card1,Card2):
    listDisplay=[]
    for key,value in fromBack.items():
      if(key==Card1 or key==Card2):
        s=str(key)+str(fromFront.get(key))
        listDisplay.append(s)
      else:
        s=str(key)+str(value)
        listDisplay.append(s)
      if len(listDisplay)==5:
        print(" ".join(listDisplay))
        listDisplay.clear()


class Player:
  def updateScore(self,currentPlayer,score):
    global player1Score,player2Score
    if(currentPlayer=="Player1"):
      player1Score+=score
    else:
      player2Score+=score
    print("Player 1 score - {}\n".format(player1Score))
    print("Player 2 score - {}\n".format(player2Score))
    if(player1Score>player2Score):
      return player1Score
    else:
      return player2Score
  
  def finalWinner(self):
    global player1Score,player2Score
    print("The Score of Player 1 is {}".format(player1Score))
    print("The Score of Player 2 is {}".format(player2Score))
    if(player1Score>player2Score):
      print("Player 1 wins")
    elif(player1Score<player2Score):
      print("Player 2 wins")
    else:
      print("The Game draws")

def firstCard():
  print("\nEnter the first card number from the range 00 to 19\n")
  Card1=input()
  return Card1

def secondCard():
  print("\nEnter the second card number from the range 00 to 19\n")
  Card2=input()
  return Card2

listtemp=[]
class MemoryGame:
  
  def startGame(self):  
    Card1=firstCard()
    while(Card1 in listtemp):
      print("You cannot play again the same card")
      Card1=firstCard()
    while((Card1 not in fromFront) or (Card1 in listtemp)):
      print("Please enter from the range 00 to 19")
      Card1=firstCard()
    
    Card2=secondCard()
    while(Card2 in listtemp):
      print("You cannot play again the same card")
      Card2=secondCard()
    while((Card2 not in fromFront) or (Card2 in listtemp)):
      print("Please enter from the range 00 to 19")
      Card2=secondCard()
    if(fromFront.get(Card1)==fromFront.get(Card2)):
      listtemp.append(Card1)
      listtemp.append(Card2)
    
    return Card1,Card2,len(listtemp)

  def playing(self,Card1,Card2):
    score=0
    result=0
    if(fromFront.get(Card1)==fromFront.get(Card2)):
      dictTemp[Card1]="[----]"
      dictTemp[Card2]="[----]"
      score=1;
      print("CONGRATS YOU WON THIS ROUND !!!! Play Again\n")
      print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
      result=1
    else:
      print("AWWW YOU LOSE THIS ROUND !!!! Next player's turn\n")
      print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
      result=0
      
    return score,result
  # def playGame():

def gameplay(player):
  cardsDone=0
  objMemoryGame=MemoryGame()
  objPlayer=Player()
  objCard=Card()
  print("\n")
  objCard.displayFirst()
  print("\n\n")
  card1,card2,cardsDone=objMemoryGame.startGame()
  print("\n\n")
  objCard.afterPlayShow(card1,card2)
  print("\n\n")
  score,result=objMemoryGame.playing(card1,card2)
  playerscore=objPlayer.updateScore(player,score)
  return result,cardsDone,int(playerscore)

def initial(firstWinPoints):
 objPlayer=Player()
 objCard=Card()
 player=""
 print("*************************--------------------WELCOME TO THE MEMORY GAME--------------------------************************")
 print("------------------------------------- The fOllowing Deck will be shown only once --------------------------------------\n")
 objCard.deckShow()
 print("\n---------- You have to remember and guess from above the correct number which has the same cards ----------------------\n")
 print("\n\n------------------------------------------------- Lets Start with toss ------------------------------------------------\n")
 toss = randint(0, 1)
 if(toss==0):
   player=listofPlayers[0]
   print("---------------------------------------------Player 1 won the toss please play first------------------------------------------")
 else:
   player=listofPlayers[1]
   print("---------------------------------------------Player 2 won the toss please play first------------------------------------------")
 cards=0
 firstPlayerReached=0
 currentPlayerIndex=0
 totalRounds=10
 while(cards!=totalRounds):
   result,cardsDone,playerscore=gameplay(player)
   cards=cardsDone/2
   if(cards==totalRounds or playerscore==firstWinPoints):
     break
   if result!=1:
     currentPlayerIndex=listofPlayers.index(player)
     if currentPlayerIndex==0:
       player=listofPlayers[1]
     else:
       player=listofPlayers[0]
   else:
     player=player
   print("------------------"+player+" is playing -----------------------------")

def declareWinner():
  objPlayer=Player()
  print("*************************************************************")

  objPlayer.finalWinner()
  print("\n*************************************************************")

initial(3)
declareWinner()




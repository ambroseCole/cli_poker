starting_amt = 100
ante = 5

num_players = int(input("How many players?"))
print("Enter players in order")
players = {input():starting_amt for _ in range(num_players)}
currentplayers = []
for i in players:
    currentplayers.append(i)
dealer = 0
callamount = 0



def roundr():
      smallblind = (dealer + 1) % num_players
      big_blind = (dealer + 2) % num_players
      currentplayer = smallblind
      currentplayers = []
      for i in players:
        currentplayers.append(i)
      pot = 0
      for i in players:
        pot += 5
        players[i] -= 5

      callamount = 0
      
      while len(currentplayers) > 1:
        print(currentplayers[currentplayer] + " Has " + str(players[currentplayers[currentplayer]]))
        cpa = input("what will "+ currentplayers[currentplayer] + " do? ")
        if cpa == "call":
            players[currentplayers[currentplayer]] -= callamount
            pot += callamount
            
            if callamount == 0:
                print("hmmm, it seems a bet hasn't been made yet. Try using the 'bet' command instead")
            else: 
                if currentplayer == len(currentplayers) - 1:
                    currentplayer = 0
                else: 
                    currentplayer += 1
        elif cpa == "raise":
            callamount = int(input("What shall the bet be raised to? "))
            players[currentplayers[currentplayer]] -= callamount
            pot += callamount
            if currentplayer == len(currentplayers) - 1:
                currentplayer = 0
            else: 
                currentplayer += 1
        elif cpa == "fold":
            currentplayers.remove(currentplayers[currentplayer])
            if currentplayer == len(currentplayers) - 1:
                currentplayer = 0
            else: 
                currentplayer += 1
        elif cpa == "bet":
            callamount = int(input("What shall the bet be? "))
            players[currentplayers[currentplayer]] -= callamount
            pot += callamount
            if currentplayer == len(currentplayers) - 1:
                currentplayer = 0
            else: 
                currentplayer += 1
        elif cpa == "add":
            namem = input("What will the new player's name be?")
            players[namem] = 100
        elif cpa == "check":
            pass
            if currentplayer == len(currentplayers) - 1:
                currentplayer = 0
            else: 
                currentplayer += 1
      for i in currentplayers:
          players[i] += pot
      checkforoutofmoney()
      
     
def checkforoutofmoney():
      for i in players:
            if players[i] <= 0:
                players.pop(i)
                
while(True):
    roundr()

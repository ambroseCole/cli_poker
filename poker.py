starting_amt = 100
ante = 5

num_players = input("How many players?")
print("Enter players in order")
players = {input():starting_amt for _ in range(num_players)}

dealer = 0

while len(players) > 1:
    pot = 0
    small_blind = (dealer + 1) % num_players
    big_blind = (dealer + 2) % num_players




    dealer = small_blind

print(players.keys()

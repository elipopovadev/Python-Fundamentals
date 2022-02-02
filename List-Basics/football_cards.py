def print_team_length(teamA, teamB):
     print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")
    

cards = input().split(" ")
teamA = [1,2,3,4,5,6,7,8,9,10,11]
teamB = [1,2,3,4,5,6,7,8,9,10,11]
game_is_terminated = False

for card in cards:
    team = card.split('-')[0]
    player = int(card.split('-')[1])
    if team == 'A' and player in teamA: 
        teamA.remove(player)
    elif team == 'B' and player in teamB:
        teamB.remove(player)
    if len(teamA) < 7 or len(teamB) < 7:
        print_team_length(teamA, teamB)
        print("Game was terminated")
        game_is_terminated = True
        break

if game_is_terminated == False:
      print_team_length(teamA, teamB)
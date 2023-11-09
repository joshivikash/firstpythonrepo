# Team A
team_A_first_inns_score = int(input())
team_A_first_inns_wickets = int(input())
team_A_second_inns_score = int(input())
team_A_second_inns_wickets = int(input())
total_score_of_team_A = team_A_first_inns_score + team_A_second_inns_score
# Team B
team_B_first_inns_score = int(input())
team_B_first_inns_wickets = int(input())
team_B_second_inns_score = int(input())
team_B_second_inns_wickets = int(input())
total_score_of_team_B = team_B_first_inns_score + team_B_second_inns_score

# Team A wins
if(total_score_of_team_A > total_score_of_team_B and team_B_second_inns_wickets == 10):
  print('Team A')
# Team B wins
elif(total_score_of_team_B > total_score_of_team_A):
  print('Team B')
else:
  print('DRAW')
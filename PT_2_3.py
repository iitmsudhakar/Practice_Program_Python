# Test Match result program

# function to check winner based on Runs 

def _calculatio_(r1,r2,r3,r4):
    Team_A_Total = r1 + r2
    Team_B_Total = r3 + r4
    if Team_A_Total > Team_B_Total:
        return True # Team A scored more
    else:
        return False # Team B scored more

# function to check wickets

def _wickets(W):
    if W == 10:
        return True # team A winner
    else:
        return False # team B winner

# function to check draw

def _draw_(r1,r2,r3,r4,W):
    Team_A_Total = r1 + r2
    Team_B_Total = r3 + r4
    if Team_A_Total == Team_B_Total or W != 10:
        return True
    else:
        return False



# Team A inputs
Team_A_runs_first_inn = int(input())
Team_A_wickets_first_inn = int(input())
Team_A_runs_second_inn = int(input())
Team_A_wickets_second_inn = int(input())

# Team B inputs
Team_B_runs_first_inn = int(input())
Team_B_wickets_first_inn = int(input())
Team_B_runs_second_inn = int(input())
Team_B_wickets_second_inn = int(input())

# logic & output

if _calculatio_(Team_A_runs_first_inn,Team_A_runs_second_inn,Team_B_runs_first_inn,Team_B_runs_second_inn) and _wickets(Team_B_wickets_second_inn):
    print("Team A")
elif not _calculatio_(Team_A_runs_first_inn,Team_A_runs_second_inn,Team_B_runs_first_inn,Team_B_runs_second_inn):
    print("Team B")
elif _draw_(Team_A_runs_first_inn,Team_A_runs_second_inn,Team_B_runs_first_inn,Team_B_runs_second_inn,Team_B_wickets_second_inn):
    print("DRAW")
else:
    print("Team B")
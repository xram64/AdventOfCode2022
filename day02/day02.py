#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2022   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  2  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 9241            |            #
#            |  `-----------'   Part 2: 14610           |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

from enum import Enum

class Throw(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Outcome(Enum):
    Loss = 0
    Draw = 3
    Win = 6

ThrowCode = {"A": Throw.Rock, "B": Throw.Paper, "C": Throw.Scissors}
ResponseCode = {"X": Throw.Rock, "Y": Throw.Paper, "Z": Throw.Scissors}


with open("day02_input.txt") as f:
    rounds = f.readlines()

#╷----------.
#│  Part 1  │
#╵----------'
response_strat_totals = {"Losses": 0, "Draws": 0, "Wins": 0, "Score": 0}

for rnd in rounds:
    throw, response = rnd.split()
    
    response_score = ResponseCode[response].value
    
    match ((ResponseCode[response].value - ThrowCode[throw].value + 1) % 3) - 1:
        case -1:
            outcome_score = Outcome.Loss.value
            response_strat_totals["Losses"] += 1
        case 0:
            outcome_score = Outcome.Draw.value
            response_strat_totals["Draws"] += 1
        case 1:
            outcome_score = Outcome.Win.value
            response_strat_totals["Wins"] += 1
    
    round_score = response_score + outcome_score
    response_strat_totals["Score"] += round_score
    
print(f"[Part 1] Total score following the first strategy guide is {response_strat_totals['Score']}. ({response_strat_totals['Wins']} wins, {response_strat_totals['Draws']} draws, {response_strat_totals['Losses']} losses)")


#╷----------.
#│  Part 2  │
#╵----------'
GoalCode = {"X": Outcome.Loss, "Y": Outcome.Draw, "Z": Outcome.Win}

goal_strat_totals = {"Losses": 0, "Draws": 0, "Wins": 0, "Score": 0}

for rnd in rounds:
    throw, goal = rnd.split()
    
    match GoalCode[goal]:
        case Outcome.Loss:
            response_score = ((ThrowCode[throw].value - 2) % 3) + 1
            goal_strat_totals["Losses"] += 1
        case Outcome.Draw:
            response_score = ThrowCode[throw].value
            goal_strat_totals["Draws"] += 1
        case Outcome.Win:
            response_score = (ThrowCode[throw].value % 3) + 1
            goal_strat_totals["Wins"] += 1
    
    outcome_score = GoalCode[goal].value
    
    round_score = response_score + outcome_score
    goal_strat_totals["Score"] += round_score
    
print(f"[Part 2] Total score following the second strategy guide is {goal_strat_totals['Score']}. ({goal_strat_totals['Wins']} wins, {goal_strat_totals['Draws']} draws, {goal_strat_totals['Losses']} losses)")


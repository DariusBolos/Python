from module3.result import winRound, loseRound, printDrawing
from module3.state import currentState
import random


def menu():
    states = []
    gameType = int(input(  # gives the player the ability to choose between a best of 3 game mode and a best of 5
        """
        1 - best of 3
        2 - best of 5
        0 - exit
        """
    ))

    nrOfRounds = {
        1: 3,
        2: 5
    }

    if gameType == 0:
        return 0

    rounds = nrOfRounds[gameType]
    score = (0, 0)

    while (score[0] <= rounds // 2) and (score[1] <= rounds // 2):  # uses a dictionary to get the input from the player
        choice = int(input(
            """
            1 - rock
            2 - paper
            3 - scissors
            0 - exit
            """
        ))

        opponentChoice = random.randrange(1, 3)

        word = {  # converts the integer given by the user to the matched drawing
            1: 'rock',
            2: 'paper',
            3: 'scissors'
        }

        if choice == 0:
            break
        else:
            play = (word[choice], word[opponentChoice])
            printDrawing(play[0])
            printDrawing(play[1])

            if play[0] == play[1]:  # determines if round is lost or won for each combination of inputs
                print("Go again")
                print(f'Score: {score[0]} : {score[1]}')
            else:
                plays = {
                    ('rock', 'scissors'): winRound,
                    ('rock', 'paper'): loseRound,
                    ('paper', 'rock'): winRound,
                    ('paper', 'scissors'): loseRound,
                    ('scissors', 'rock'): loseRound,
                    ('scissors', 'paper'): winRound
                }

                plays[play](states)
                score = currentState(states)  # gets the current state of the ongoing game
                print(f'Score: {score[0]} : {score[1]}')

    print(f'Game has finished with the score: {score[0]} : {score[1]}')
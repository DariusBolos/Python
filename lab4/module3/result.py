from module3.state import currentState, newState


def winRound(states):  # updates the state in case the player has won the round
    try:
        curState = currentState(states)
        newState(states, curState[0] + 1, curState[1])
    except IndexError:
        newState(states, 1, 0)


def loseRound(states):  # updates the state in case the computer has won the round
    try:
        curState = currentState(states)
        newState(states, curState[0], curState[1] + 1)
    except IndexError:
        newState(states, 0, 1)


def printDrawing(option):  # prints rock paper or scissors to the screen
    drawings = {
        'rock': """
                    _______
                ---'   ____)
                      (_____)
                      (_____)
                      (____)
                ---.__(___)
                """,
        'paper': """
                     _______
                ---'    ____)____
                           ______)
                          _______)
                         _______)
                ---.__________)
                """,
        'scissors': """
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
                """
    }

    print(drawings[option])


def winGame(curState, maxRounds):  # function called when a game is won by the player containing a winning message
    if curState[0] > maxRounds // 2:
        print('Congrats, you have won!')


def loseGame(curState, maxRounds):  # function called when a game is won by the player containing a losing message
    if curState[1] > maxRounds // 2:
        print('You have lost, try again!')
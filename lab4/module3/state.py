def currentState(states):  # gets the current state of the game
    return states[-1]


def newState(states, playerScore, opponentScore):  # adds a new state to the states list
    newResult = (playerScore, opponentScore)
    states.append(newResult)
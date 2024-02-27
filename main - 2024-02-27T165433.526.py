import numpy as np
from itertools import combinations

# Define the characteristic function for the cooperative game
def characteristic_function(coalition):
    """
    Characteristic function representing the worth of each coalition.

    Parameters:
    coalition (list): List of players in the coalition.

    Returns:
    float: Worth of the coalition.
    """
    return len(coalition) ** 2  # Example: worth is proportional to the square of the coalition size

# Define the players and their cognitive biases
players = {
    'Alice': 0.8,   # Bias of 0.8: Alice overestimates the worth of coalitions
    'Bob': 1.0,     # No bias: Bob evaluates the worth of coalitions accurately
    'Charlie': 0.6  # Bias of 0.6: Charlie underestimates the worth of coalitions
}

# Calculate the worth of all possible coalitions
coalitions = []
for i in range(1, len(players) + 1):
    coalitions.extend(list(combinations(players.keys(), i)))

worths = {}
for coalition in coalitions:
    worth = characteristic_function(coalition)
    worths[coalition] = worth

# Determine the stable coalition structure
stable_coalitions = []
for coalition in coalitions:
    worth = worths[coalition]
    for player in coalition:  # Iterate over players in the coalition
        bias = players[player]
        if worth * bias > sum(worths[c] for c in coalitions if player in c):
            break
    else:
        stable_coalitions.append(coalition)

# Print the stable coalition structure
print("Stable Coalitions:")
for coalition in stable_coalitions:
    print(coalition)

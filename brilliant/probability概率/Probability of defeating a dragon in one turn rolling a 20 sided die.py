# https://stats.stackexchange.com/questions/549334/probability-of-defeating-a-dragon-in-one-turn-rolling-a-20-sided-die


import numpy as np

def markov_matrix(hp ,num_sides):
    # P is the transition matrix.
    # Need one state for each hp of the dragon, plus a 'player dies' state and a 'dragon dies' state
    # States 0-hp are damage done states, state -2 is 'player dies', state -1 is 'dragon dies'
    P = []

    for damage_done in range(hp):
        P_row = np.zeros(hp +2)

        # For each state, the probability for the player to die is 1/num_sides.
        P_row[-2] = 1/ num_sides

        # Otherwise, there is an equal probability to deal 2 or more damage.
        for hit_damage in range(2, num_sides):
            new_state_index = damage_done + hit_damage

            # If the total damage would be enough to kill the dragon, that probability is added to the 'dragon dies' state.
            if new_state_index >= hp:
                P_row[-1] = P_row[-1] + 1 / num_sides
            else:
                P_row[new_state_index] = 1 / num_sides

        # If a crit is rolled, the dragon is immune.
        P_row[damage_done] = 1 / num_sides

        P.append(P_row)
    # The 'player dies' and 'dragon dies' states are absorbing.
    player_dies_row = np.zeros(hp + 2)
    player_dies_row[-2] = 1
    P.append(player_dies_row)

    dragon_dies_row = np.zeros(hp + 2)
    dragon_dies_row[-1] = 1
    P.append(dragon_dies_row)

    P = np.stack(P)
    return P


def probability_of_dragon_death(hp, num_sides, max_num_attacks):
    P = markov_matrix(hp, num_sides)
    initial_state_probabilities = np.zeros(hp + 2)

    # Initially we are in the 0 damage done state with 100% probability.
    initial_state_probabilities[0] = 1

    final_state_probabilities = initial_state_probabilities @ (np.linalg.matrix_power(P, max_num_attacks))
    return final_state_probabilities[-1]

print(probability_of_dragon_death(hp, num_sides, max_num_attacks))
'''
Running the function probability_of_dragon_death(hp=250,num_sides=20,max_num_attacks=10000) 
returns a probability of ≈0.269880.

For fun, I've also attached a figure showing your probability to defeat the 
dragon when given its HP.
'''
import random

from check import check
from word_list import poop_list, word_list

# now = datetime.datetime.now()
# random.seed(str(now)[:-15])


def pick(game_mode):

    # match game_diff:
    #    case "normal":
    #        difficulty = 5
    #    case "hard":
    #        difficulty = 8
    #    case "impossible":
    #        difficulty = 12
    #    case _:
    #        difficulty = 5

    match game_mode:
        case "poop":
            goal_word = random.choice(poop_list)
        case "chaos":
            goal_word = random.choice(word_list)
        case _:
            goal_word = game_mode

    first_word = random.choice(word_list)
    return first_word, goal_word

import datetime
import random

# from check import check
from word_list import poop_list, word_list


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
        case "custom":
            goal_word = mode_custom()
        case "daily":
            goal_word = mode_daily()
        case _:
            goal_word = "poop"

    first_word = random.choice(word_list)
    return first_word, goal_word


def mode_custom():
    print("pick custom word")
    x = input().lower()
    if x in word_list:
        return x
    else:
        print("invalid word")
        mode_custom()


def mode_daily():
    now = datetime.datetime.now()
    random.seed(str(now)[:-15])
    x = random.choice(range(0, 2))
    match x:
        case 0:
            return random.choice(poop_list)
        case _:
            return random.choice(word_list)

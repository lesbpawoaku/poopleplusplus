import datetime
import random

from scale_path import word_path as scale_path

# from check import check
from word_list import poop_list, word_list


def pick(game_diff, game_mode):
    match game_diff:
        case "normal":
            difficulty = 5
        case "hard":
            difficulty = 8
        case "impossible":
            difficulty = 10
        case _:
            difficulty = 5

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
    print("Finding suitable word!\n(Might take longer on harder difficulties)")
    first_word = scale_path(goal_word, difficulty)
    print(f"Word chosen: {first_word}")
    return first_word, goal_word


def mode_custom():
    print("pick custom word")
    x = input().lower()
    if x in word_list:
        return x
    else:
        print("invalid word")
        return mode_custom()


def mode_daily():
    now = datetime.datetime.now()
    random.seed(str(now)[:-15])
    x = random.choice(range(0, 2))
    match x:
        case 0:
            return random.choice(poop_list)
        case _:
            return random.choice(word_list)

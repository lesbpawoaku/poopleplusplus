import datetime
import random

from check import check
from word_list import word_list

now = datetime.datetime.now()
random.seed(str(now)[:-15])


def pick():
    goal_word = random.choice(word_list)
    new_word = random.choice(word_list)

    def new_word_check(new_word, goal_word, words_away):
        if words_away > 5:
            checker = check(new_word, goal_word, goal_word)
            match checker:
                case "valid":
                    new_word_check(random.choice(word_list), new_word, words_away + 1)
                case _:
                    new_word_check(random.choice(word_list), goal_word, words_away)
        else:
            return new_word

    first_word = new_word_check(new_word, goal_word, 0)
    return first_word, goal_word

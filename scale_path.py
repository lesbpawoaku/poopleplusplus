import random

from word_list import word_list

visited = []


def new_word(word):
    global visited
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        i = random.randint(0, 3)
        char = random.randint(0, 25)
        new_char = alphabet[char]
        new_word = "%s%s%s" % (word[:i], new_char, word[i + 1 :])
        if new_word in word_list and new_word not in visited:
            visited.append(new_word)
            return new_word


def new_path(diff, goal):
    global visited
    visited = [goal]
    curr = goal
    for i in range(diff):
        curr = new_word(curr)
    return visited[-1]

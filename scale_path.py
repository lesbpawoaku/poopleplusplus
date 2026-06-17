import random
from collections import deque

from word_list import word_list


def new_words(word):
    global visited
    words = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(4):
        for char in alphabet:
            if char != word[i]:
                words.append("%s%s%s" % (word[:i], char, word[i + 1 :]))
    random.shuffle(words)
    for word in words:
        yield word


def word_path(end, diff):
    global visited
    queue = deque([end])
    visited = {end}
    parent = {end: None}
    while queue:
        word = queue.popleft()
        path = []
        curr = word
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        if diff == len(path) - 1:
            return word
        for new_word in new_words(word):
            if new_word in word_list and new_word not in visited:
                visited.add(new_word)
                parent[new_word] = word
                queue.append(new_word)

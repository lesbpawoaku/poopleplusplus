from collections import deque

from word_list import word_list


def new_words(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(4):
        for char in alphabet:
            if char != word[i]:
                yield "%s%s%s" % (word[:i], char, word[i + 1 :])


def word_path(start, end):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    while queue:
        word = queue.popleft()
        if word == end:
            path = []
            while word is not None:
                path.append(word)
                word = parent[word]
            return path[::-1]
        for new_word in new_words(word):
            if new_word in word_list and new_word not in visited:
                visited.add(new_word)
                parent[new_word] = word
                queue.append(new_word)


print(word_path("unai", "gang"))

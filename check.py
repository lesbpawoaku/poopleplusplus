from word_list import all_words


def check(input_word, curr_word, goal_word):
    matches = 0
    goal_letters = 0
    if input_word == curr_word:
        return "same word"
    elif len(input_word) < 4:
        return "too short"
    elif len(input_word) > 4:
        return "too long"
    elif input_word not in all_words:
        return "not listed"
    else:
        for i, char in enumerate(input_word):
            if char == curr_word[i]:
                matches += 1
            if char == goal_word[i]:
                goal_letters = i

        if matches != 3:
            return "not enough"
        else:
            if input_word == goal_word:
                return "win"
            else:
                return "valid"

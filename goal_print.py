def goal_print(curr_word, goal_word):
    the_print = ""
    for i in range(0, 4):
        if curr_word[i] == goal_word[i]:
            the_print += f"[{curr_word[i]}] "
        else:
            the_print += f"({curr_word[i]}) "
    return the_print

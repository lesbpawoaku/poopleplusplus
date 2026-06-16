from gameplay import play
from pickwords import pick


def main():
    curr_word, goal_word = pick()
    the_print = f"GOAL: {goal_word} \n({curr_word[0]}) ({curr_word[1]}) ({curr_word[2]}) ({curr_word[3]})"
    guesses = 0
    play(curr_word, goal_word, the_print, guesses)


if __name__ == "__main__":
    main()

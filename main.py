from gameplay import play
from pickwords import pick
from startup import startup


def main():
    game_diff, game_mode = startup()

    curr_word, goal_word = pick(game_diff, game_mode)
    the_print = f"GOAL: {goal_word} \n({str(curr_word)[0]}) ({str(curr_word)[1]}) ({str(curr_word)[2]}) ({str(curr_word)[3]})"
    guesses = 0
    play(curr_word, goal_word, the_print, guesses)


if __name__ == "__main__":
    main()

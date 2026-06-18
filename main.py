from gameplay import play
from goal_print import goal_print
from pick_modes import pick
from startup import startup


def main():
    game_mode, game_diff = startup()
    curr_word, goal_word = pick(game_diff, game_mode)
    the_print = f"GOAL: [{goal_word}] \n{goal_print(curr_word, goal_word)}"
    guesses = 0
    print(f'get to "{goal_word.upper()}" in as few steps as possible\n.\n.\n.\n.\n.\n.')
    play(curr_word, goal_word, the_print, guesses)


if __name__ == "__main__":
    main()

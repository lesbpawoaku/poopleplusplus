from check import check
from goal_print import goal_print


def play(curr_word, goal_word, the_print, guesses):
    print(the_print)
    input_word = input().lower()
    checked = check(input_word, curr_word, goal_word)
    match checked:
        case "same word":
            print("word is the same")
            play(curr_word, goal_word, the_print, guesses)
        case "canceled":
            print("canceled!!")
        case "too short":
            print("word is too short")
            play(curr_word, goal_word, the_print, guesses)
        case "too long":
            print("word is too long")
            play(curr_word, goal_word, the_print, guesses)
        case "not listed":
            print("not in word list")
            play(curr_word, goal_word, the_print, guesses)
        case "not enough":
            print("not one letter different")
            play(curr_word, goal_word, the_print, guesses)
        case "valid":
            new_print = the_print + f"\n{goal_print(input_word, goal_word)}"
            play(input_word, goal_word, new_print, guesses + 1)
        case "win":
            print(
                f"{the_print} \n[{input_word[0]}] [{input_word[1]}] [{input_word[2]}] [{input_word[3]}] \nyou win!! GUESSES: {guesses + 1}"
            )
        case _:
            print("error")
            play(curr_word, goal_word, the_print, guesses)

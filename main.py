from check import check

guesses = 0
curr_word = "yuri"
goal_word = "turd"
the_print = f"GOAL: {goal_word} \n({curr_word[0]}) ({curr_word[1]}) ({curr_word[2]}) ({curr_word[3]})"


def main(curr_word, goal_word, the_print, guesses):
    print(the_print)
    input_word = input().lower()
    checked = check(input_word, curr_word, goal_word)
    match checked:
        case "same word":
            print("word is the same")
            main(curr_word, goal_word, the_print, guesses)
        case "too short":
            print("word is too short")
            main(curr_word, goal_word, the_print, guesses)
        case "too long":
            print("word is too long")
            main(curr_word, goal_word, the_print, guesses)
        case "not listed":
            print("not in word list")
            main(curr_word, goal_word, the_print, guesses)
        case "not enough":
            print("not one letter different")
            main(curr_word, goal_word, the_print, guesses)
        case "valid":
            new_print = (
                the_print
                + f"\n({input_word[0]}) ({input_word[1]}) ({input_word[2]}) ({input_word[3]})"
            )
            main(input_word, goal_word, new_print, guesses + 1)
        case "win":
            print(
                f"{the_print} \n({input_word[0]}) ({input_word[1]}) ({input_word[2]}) ({input_word[3]}) \nyou win!! GUESSES: {guesses + 1}"
            )
        case _:
            print("error")
            main(curr_word, goal_word, the_print)


if __name__ == "__main__":
    main(curr_word, goal_word, the_print, guesses)

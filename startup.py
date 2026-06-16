from word_list import word_list


def startup():

    # def difficulty():
    #    print("select difficulty\n(NORMAL) (HARD) (IMPOSSIBLE) 1-3")
    #    x = str(input().lower())
    #   print(x)
    #    match x:
    #        case "normal" | "1":
    #            return "normal"
    #        case "hard" | "2":
    #            return "hard"
    #        case "impossible" | "3":
    #            return "impossible"
    #        case _:
    #            print("invalid difficulty")
    #            difficulty()

    def mode():
        print("select mode\n(POOP) (CHAOS) (CUSTOM) 1-3")
        x = input().lower()
        match x:
            case "poop" | "1":
                return "poop"
            case "chaos" | "2":
                return "chaos"
            case "custom" | "3":
                mode_custom()
            case _:
                print("invalid mode")
                mode()

    def mode_custom():
        print("pick custom word")
        x = str(input().lower())
        if x in word_list:
            return x
        else:
            print("invalid word")
            mode_custom()

    game_mode = mode()
    return game_mode

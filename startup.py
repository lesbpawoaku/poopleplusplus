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

    def pick_mode():
        print("select mode\n(POOP) (CHAOS) (DAILY) (CUSTOM) 1-4")
        x = input().lower()
        match x:
            case "poop" | "1":
                return "poop"
            case "chaos" | "2":
                return "chaos"
            case "daily" | "3":
                return "daily"
            case "custom" | "4":
                return "custom"
            case _:
                print("invalid mode")
                pick_mode()

    game_mode = pick_mode()
    return game_mode

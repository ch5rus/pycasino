def fmt(input, arg):  # Formats strings, e.g., highlights money values.
    input = str(input)
    arg = str(arg)
    match arg:
        case "money":
            return f"\033[32;1;4m${input}\033[0m"  # Highlights bright green, bold and underlined, with a dollar symbol concatenated.
        case "num":
            return f"\033[93;1;4m{input}\033[0m"  # Highlights bright yellow, bold and underlined.
        case "terminal input":
            return f"\033[96;1m{input}\033[0m"  # Highlights bright cyan, bold.
        case "_":
            return None
def clear():
    import os
    os.system("cls" if os.name == "nt" else "clear")

# ^ module functions
# v main

if __name__ == "__main__":
    import slots
    import highlow
    import os
    import json
    os.system("color")

    try:
        if not os.path.isfile("conf.json"): # Checks if the file exists: if not, creates it.
            with open("conf.json", "w") as temp:
                json.dump({"bank": 1000}, temp, indent=4) # Default bank value
        with open("conf.json", "r") as temp: # Retrieves bank value to be edited during runtime
            conf = json.load(temp)
            bank = conf["bank"]

        # Mainloop begins here

        gamestate = True
        while gamestate:
            gameselection = input(f"Welcome to the casino.\nYour current bank value is {fmt(bank, "money")}.\n\nWhat game do you wish to play?\n\n{fmt(">(21, highlow, slots, poker, or exit?)", "terminal input")} ").strip().lower()
            match gameselection:
                case "exit" | "e":
                    break
                case "slots" | "s":
                    playercontinue = True
                    while playercontinue:
                        bank = slots.slot_game(bank)
                        yn = input(f"Would you like to continue?\n\n{fmt(">(y/n)", "terminal input")}").strip().lower()
                        playercontinue = yn == "y"
                    clear()
                case "highlow" | "h":
                    playercontinue = True
                    while playercontinue:
                        bank = highlow.highlow_game(bank)
                        yn = input(f"Would you like to continue?\n\n{fmt(">(y/n)", "terminal input")}").strip().lower()
                        playercontinue = yn == "y"

        # Mainloop ends here

        with open("conf.json", "w") as temp: # Writes the new bank value to disk.
            conf["bank"] = bank
            json.dump(conf, temp, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")

    input(fmt("\nPress ENTER to exit", "terminal input"))
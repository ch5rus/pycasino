def fmt(input, arg):  # Formats strings, e.g., highlights money values.
    input = str(input)
    arg = str(arg)
    match arg:
        case 'money':
            return f'\033[93;1;4m${input}\033[0m'  # Highlights bright yellow, bold and underlined.
        case 'terminal input':
            return f'\033[96;1m{input}\033[0m'  # Highlights bright cyan, bold.
        case '_':
            return None
def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# ^ module functions
# v main

if __name__ == '__main__':
    import slots
    import os
    os.system('color')

    try:
        if not os.path.isfile('bank.txt'): # Create bank.txt with default balance if it doesn't exist
            with open('bank.txt', 'w') as temp:
                temp.write('1000')  # Default bank value

        with open('bank.txt', 'r') as temp: # Retrieves bank value to be edited during runtime
            bank = int(temp.read())

        # Mainloop begins here

        gamestate = True
        while gamestate:
            gameselection = input(f'Welcome to the casino.\nYour current bank value is {fmt(bank, "money")}.\n\nWhat game do you wish to play?\n\n{fmt('>(21, highlow, slots, or exit?)', 'terminal input')} ')
            match gameselection:
                case 'exit':
                    break
                case 'slots':
                    playercontinue = True
                    while playercontinue == True:
                        bank = slots.slots(bank)
                        yn = input(f'Would you like to continue?\n\n>(y/n)')
                        playercontinue = yn == 'y'
                    clear()

        # Mainloop ends here

        with open('bank.txt', 'w') as temp: # Writes the new bank value to disk.
            temp.write(str(bank))

    except Exception as e:
        print(f"An error occurred: {e}")

    input(fmt('Press ENTER to exit', 'terminal input'))
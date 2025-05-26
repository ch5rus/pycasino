from casino import clear
from casino import fmt
import random as rand

def highlow_game(bank):
    clear()
    answer = rand.randint(1,100)
    estimate = rand.randint(1,100)
    while True:
        try:
            deposit = int(input(f"Your current balance is {fmt(bank, "money")}.\nHow much would you like to deposit?\n\n{fmt(">(int)", "terminal input")} "))
            break
        except ValueError:
            print(f"\n{fmt("Please enter an integer!", "terminal input")}\n")
    while True:
        try:
            guess = input(f"\nDo you think the true value is higher, equal or lower than {fmt(estimate, "num")}?\n\n{fmt(">(h, e, l)", "terminal input")}").strip().lower()
            if guess not in {"h", "e", "l"}:
                raise Exception
            break
        except Exception:
            print(f"\n{fmt("Please enter a valid answer!", "terminal input")}")
    if (
            (guess == 'h' and answer > estimate) or
            (guess == 'e' and answer == estimate) or
            (guess == 'l' and answer < estimate)
    ):
        print(f"\nJackpot! The true number was {answer}")
        print(f"Deposit of {fmt(deposit, "money")} added to bank!")
        bank = bank + deposit
        print(f"You have {fmt(bank, "money")} in your bank!")
    else:
        print(f"\nNo luck! The true number was {answer}")
        print(f"Deposit of {fmt(deposit, "money")} subtracted from bank!")
        bank = bank - deposit
        print(f"You have {fmt(bank, "money")} in your bank!")
    return bank

if __name__ == "__main__":
    highlow_game(100)
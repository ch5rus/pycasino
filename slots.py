from casino import clear
from casino import fmt
import random
from time import sleep

def slots(bank):
    clear()
    deposit = int(input(f'Your current balance is {fmt(bank, "money")}.\nHow much would you like to deposit?\n\n{fmt('>(int)', 'terminal input')} '))
    for i in range(2): # Won't work in pycharm/vscode debugging, aka IDLE. Only shows through running the .py.
        print('                   ', end='\r')
        print('Spinning.',end='\r')
        sleep(0.2)
        print('Spinning..', end='\r')
        sleep(0.2)
        print('Spinning...', end='\r')
        sleep(0.2)
    print('')

    class fruits:
        cherry = 'cherry'
        lemon = 'lemon'
        grape = 'grape'
    index = ['7', 'star', 'star', fruits.cherry, fruits.lemon, fruits.grape]
    x, y, z = random.choice(index), random.choice(index), random.choice(index)
    a = [x, y, z] # packs the slots into a list so it can be checked for jackpot
    b = [hasattr(fruits, index[index.index(x)]), # checks if any of the slots belong to the fruits class, returning a bool
         hasattr(fruits, index[index.index(y)]),
         hasattr(fruits, index[index.index(z)])]

    print(f'[{x}][{y}][{z}]')

    if a == ['7', '7', '7']: # all sevens jackpot
        print('7 jackpot')
        print(f'Deposit of {fmt(deposit, 'money')} doubled to {fmt(deposit * 2, 'money')} and added to bank!')
        deposit = deposit * 2
        bank = bank + deposit
        print(f'You have {fmt(bank, 'money')} in your bank!')

    elif a == ['star', 'star', 'star']: # all stars jackpot
        print('star jackpot')
        print(f'Deposit of {fmt(deposit, 'money')} multiplied by 1.5 to {fmt(deposit * 1.5, 'money')} and added to bank!')
        deposit = deposit * 1.5
        bank = bank + deposit
        print(f'You have {fmt(bank, 'money')} in your bank!')

    elif b == [True, True, True]: # all fruits jackpot
        print('All fruits')
        print(f'Deposit of {fmt(deposit, 'money')} multiplied by 1.2 to {fmt(deposit * 1.2, 'money')} and added to bank!')
        deposit = deposit * 1.2
        bank = bank + deposit
        print(f'You have {fmt(bank, 'money')} in your bank!')

    else:
        print('No luck!')
        print(f'Deposit of {fmt(deposit, 'money')} subtracted from bank!')
        bank = bank - deposit
        print(f'You have {fmt(bank, 'money')} in your bank!')

    return bank

if __name__ == '__main__': # debug
    while True:
        slots(100)
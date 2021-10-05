import time
import os

def clear():
    command = 'cls'
    os.system(command)


def stop():
    clear()
    print('De bestelling word gestopt')
    time.sleep(1)
    clear()
    exit()

def stap2(b):
    print('Om terug te gaan type: back')
    print('Om te stoppen type: quit')
    print('Wilt u de ' + str(b) + ' bolletjes in een hoorntje of een bakje? ')
    keuze = input('')
    if keuze == 'bakje':
        clear()
        bakjes(b)
    elif keuze == 'hoorntje':
        clear()
        hoorntjes(b)
    elif keuze == 'back':
        bolletjes()
    elif keuze == 'quit':
        stop()
    else:
        print('Sorry, dat snap ik niet')
        time.sleep(1)
        clear()
        return stap2(b)


def hoorntjes(b):
    print('U krijgt een hoorntje met ' + str(b) + ' bolletjes')
    time.sleep(2)
    clear()
    smaken(b)


def bakjes(b):
    print('U krijgt een bakje met ' + str(b) + ' bolletjes')
    time.sleep(2)
    clear()
    smaken(b)


def bolletjes():
    clear()
    print('Hoeveel bolletjes wilt u?')
    bolletje = int(input(''))
    if int(bolletje) <= 3:
        time.sleep(0.5)
        clear()
        stap2(bolletje)
    elif int(bolletje) <= 8:
        time.sleep(0.5)
        clear()
        bakjes(bolletje)
    elif bolletje > 8:
        print('Sorry, zulke grote bakken hebben wij niet')
        time.sleep(1)
        clear()
        return bolletjes()

def smaken(b):

    vanille = 0
    chocolade = 0
    munt = 0
    aardbij = 0

    b = b + 1
    print('Smaken:')
    print('vannille     - V')
    print('chocolade    - C')
    print('aardbij      - A')
    print('munt         - M')
    for s in range(1,b):
        smaak = input('Welke smaak wilt u voor bolletje ' + str(s) + ': ')
        if smaak == 'V':
            vanille = vanille + 1
        elif smaak == 'C':
            chocolade = chocolade + 1
        elif smaak == 'A':
            aardbij = aardbij + 1
        elif smaak == 'M':
            munt = munt + 1
        else:
            b = b - 1
            clear()
            return smaken(b)
    print('U krijgt ' + str(vanille) + ' bolletjes vanille')
    print('U krijgt ' + str(chocolade) + ' bolletjes chocolade')
    print('U krijgt ' + str(aardbij) + ' bolletjes aardbij')
    print('U krijgt ' + str(munt) + ' bolletjes munt')
    time.sleep(3)
    clear()
    bestellen()


def bestellen():
    print('Wilt u nog meer bestellen? J/N')
    bestelling = input('')
    if bestelling == 'J':
        bolletjes()
    elif bestelling == 'N':
        time.sleep(1)
        clear()
        print('Bedankt en tot ziens!')
        time.sleep(1)
        clear()
        exit()
    else:
        print('Sorry, ik snap het niet')
        time.sleep(1)
        bestellen()

print('Wekom bij Papi Gelato')
bolletjes()
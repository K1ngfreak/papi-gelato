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

def stap2(bo):

    print('Wilt u de ' + str(bo) + ' bolletjes in een hoorntje of een bakje? ')
    keuze = input('')
    if keuze == 'bakje':
        clear()
        ba = 1
        bakjes(bo,ba)
    elif keuze == 'hoorntje':
        clear()
        ho = 1
        hoorntjes(bo,ho)
    elif keuze == 'back':
        bolletjes()
    elif keuze == 'quit':
        stop()
    else:
        print('Sorry, dat snap ik niet')
        time.sleep(1)
        clear()
        return stap2(bo)


def hoorntjes(bo,ho):
    print('U krijgt een hoorntje met ' + str(bo) + ' bolletjes')
    time.sleep(2)
    clear()
    ba = 0
    smaken(bo,ba,ho)


def bakjes(bo,ba):
    print('U krijgt een bakje met ' + str(bo) + ' bolletjes')
    time.sleep(2)
    clear()
    ho = 0
    smaken(bo,ba,ho)


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
        ba = 1
        bakjes(bolletje, ba)
    elif bolletje > 8:
        print('Sorry, zulke grote bakken hebben wij niet')
        time.sleep(1)
        clear()
        return bolletjes()

def smaken(bo,ba,ho):

    vanille = 0
    chocolade = 0
    munt = 0
    aardbij = 0

    bo = bo + 1
    print('Smaken:')
    print('vannille     - V')
    print('chocolade    - C')
    print('aardbij      - A')
    print('munt         - M')
    for s in range(1,bo):
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
            bo = bo - 1
            clear()
            return smaken(bo)
    print('U krijgt ' + str(vanille) + ' bolletje(s) vanille')
    print('U krijgt ' + str(chocolade) + ' bolletje(s) chocolade')
    print('U krijgt ' + str(aardbij) + ' bolletje(s) aardbij')
    print('U krijgt ' + str(munt) + ' bolletje(s) munt')
    time.sleep(5)
    bo = bo - 1
    clear()
    toppings(bo,ba,ho)

def toppings(bo,ba,ho):
    print('Wat voor topping wilt U?')
    print('A) Geen')
    print('B) Slagroom')
    print('C) Sprinkels')
    print('D) Caramel Saus')
    topping = input('Welke topping wilt U? ')
    if topping == 'A':
        to = 0
    elif topping == 'B':
        to = 0.50
    elif topping == 'C':
        to = 0.30
    elif topping == 'D':
        if ba >= 1:
            to = 0.90
        elif ho >= 1:
            0.60
    clear()
    bestellen(bo,ba,ho,to)

def bestellen(bo,ba,ho,to):
    global bol
    global bak
    global hoorn
    global topping
    
    bol = bol + bo
    bak = bak + ba
    hoorn = hoorn + ho
    topping = topping + to

    print('Wilt u nog meer bestellen? J/N')
    bestelling = input('')
    if bestelling == 'J':
        bolletjes()
    elif bestelling == 'N':
        time.sleep(1)
        clear()
        receipt(bol,bak,hoorn,to)
    else:
        print('Sorry, ik snap het niet')
        time.sleep(1)
        bestellen()

def receipt(bo,ba,ho,to):
    boll = float(bo * 1.10)
    bakje = float(ba * 1.25)
    hoorntje = float(ho * 0.75)

    eind = float(boll + bakje + hoorntje)

    print('---------["Papi Gelato"]---------')
    if boll > 0:
        print('bolletjes    ' + str(bo) + ' X €1.10    = €' + str(boll))
    if bakje > 0:
        print('bakjes       ' + str(ba) + ' X €1.10    = €' + str(bakje))
    if hoorntje > 0:
        print('hoorntjes    ' + str(ho) + ' X €1.10    = €' + str(hoorntje))
    if to > 0:
        print('toppings     ' + str(to) + ' X €1.10    = €' + str(to))
    print('                         ---------- +')
    print('Totaal                    = €' + str(eind))

    time.sleep(5)
    print('Bedankt en tot ziens!')
    time.sleep(1)
    clear()
    exit()

bol = 0
bak = 0
hoorn = 0
topping = 0

print('Wekom bij Papi Gelato')
time.sleep(2)
bolletjes()
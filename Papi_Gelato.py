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
        print('Sorry dat is geen optie die we aanbieden...')
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
        print('Sorry dat is geen optie die we aanbieden...')
        time.sleep(1)
        clear()
        return bolletjes()

def smaken(bo,ba,ho):

    vanille = 0
    chocolade = 0
    aardbij = 0

    bo = bo + 1
    print('Smaken:')
    print('vannille     - V')
    print('chocolade    - C')
    print('aardbij      - A')
    for s in range(1,bo):
        smaak = input('Welke smaak wilt u voor bolletje ' + str(s) + ': ')
        if smaak == 'V' or smaak == 'v':
            vanille = vanille + 1
        elif smaak == 'C' or smaak == 'c':
            chocolade = chocolade + 1
        elif smaak == 'A' or smaak == 'a':
            aardbij = aardbij + 1
        else:
            print('Sorry dat is geen optie die we aanbieden...')
            bo = bo - 1
            time.sleep(1)
            clear()
            return smaken(bo)
    print('U krijgt ' + str(vanille) + ' bolletje(s) vanille')
    print('U krijgt ' + str(chocolade) + ' bolletje(s) chocolade')
    print('U krijgt ' + str(aardbij) + ' bolletje(s) aardbij')
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
    if topping == 'A' or topping == 'a':
        to = 0
        top = 1
    elif topping == 'B' or topping == 'b':
        to = 0.50
        top = 1
    elif topping == 'C' or topping == 'c':
        to = 0.30
        top = 1
    elif topping == 'D' or topping == 'd':
        if ba >= 1:
            to = 0.90
            top = 1
        elif ho >= 1:
            to = 0.60
            top = 1
    else:
        print('Sorry dat is geen optie die we aanbieden...')
    clear()
    bestellen(bo,ba,ho,to,top)

def bestellen(bo,ba,ho,to,top):
    global bol
    global bak
    global hoorn
    global topping
    global totalTopping
    
    bol = bol + bo
    bak = bak + ba
    hoorn = hoorn + ho
    topping = topping + to
    totalTopping = totalTopping + top

    print('Wilt u nog meer bestellen? J/N')
    bestelling = input('').upper()
    if bestelling == 'J':
        bolletjes()
    elif bestelling == 'N':
        time.sleep(1)
        clear()
        receipt(bol,bak,hoorn,topping,totalTopping)
    else:
        print('Sorry dat is geen optie die we aanbieden...')
        time.sleep(1)
        bestellen()

def receipt(bo,ba,ho,to,top):
    boll = float(bo * 0.95)
    bakje = float(ba * 1.25)
    hoorntje = float(ho * 0.75)

    eind = float(boll + bakje + hoorntje + to)

    print('---------["Papi Gelato"]---------')
    if boll > 0:
        print('bolletjes    ' + str(bo) + ' X €1.10    = €' + str(boll))
    if bakje > 0:
        print('bakjes       ' + str(ba) + ' X €1.10    = €' + str(bakje))
    if hoorntje > 0:
        print('hoorntjes    ' + str(ho) + ' X €1.10    = €' + str(hoorntje))
    if to > 0:
        print('toppings     ' + str(top) + ' X €1.10    = €' + str(to))
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
totalTopping = 0

print('Wekom bij Papi Gelato')
time.sleep(2)
bolletjes()
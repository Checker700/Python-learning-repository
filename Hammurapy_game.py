import random
import sys

def quit():
    print('\n\n\n Good bye\n')
    sys.exit()

def printNotEnoughGrain():
    print(f'Think one more time, you have only {grain} bushels of grain.')

def printNotEnoughLand():
    print(f'Think one more time, you have only {land} acres of land.')

def endGameBad():
    print('Your reign was terrible, \nyou were declared a national traitor and expelled from the residence!')
    quit()

def tradeLand():
    global land, grain
    cost = random.randint(17,27)
    print(f'The cost of an acre of land is {cost} bushels')
    buysell = 0
    while True:
        buysell = int(input('How much acres you want to buy/sell?'))
        if buysell < 0 and -buysell > land:
            printNotEnoughLand()
            continue

        if buysell > 0 and cost * buysell > grain:
            printNotEnoughGrain()
            continue
        break
    land = land + buysell
    grain = grain - cost * buysell

def feedPeople():
    global food, grain
    print('')
    while True:
        food = int(input('How much bushels of grain you want to spend for feeding the people?'))
        if food < 0:
            continue
        if food <= grain:
            break
        printNotEnoughGrain()
    grain = grain - food

def plantSeeds():
    global grain, harvest, harvest_total
    print('')
    plant = 0
    while True:
        plant = int(input('How much acres of land you want to seed?'))
        if plant < 0:
            continue
        if plant > land:
            printNotEnoughLand()
            continue
        if plant / 2 > grain:
            continue
        if plant > 10 * population:
            print(f'But you have only {population} for work on fields')
            continue
        break
    grain = grain - plant // 2
    harvest = random.randint(1, 6)
    harvest_total = plant * harvest

def ratsInvasion():
    global rats, grain
    rats = 0
    c = random.randint(1, 6)
    if c % 2 == 0:
        rats = grain // c
    grain -= rats

def harvestGrain():
    global grain
    grain = grain + harvest_total

def changePopulation():
    global people_came, population, starved, percent_died, died_total
    people_came = random.randint(1, 6) * (20 * land + grain) // population // 100 + 1
    starved = population - food // 20
    if starved <= 0:
        starved = 0
    else:
        if starved > 0.45 * population:
            print(f'\n For the last year {starved} people died of starving')
            endGameBad()
        percent_died = ((year - 1) * percent_died + starved * 100 // population) // year
        population = population - starved
        died_total = died_total + starved
    population = population + people_came

def plague():
    global year, population
    if year > 1 and random.randint(0, 99) < 15:
        population -= population // 2
        print('/n Plague! Half of the people died!')
def report():
    print('\n Your majesty, here is my report:')
    print(f'Last year ({year}): {starved} people died of starving, {people_came} people came to the city.')
    print(f'{population} people lives in the city now.')
    print(f'The city owns {land} acres of land.')
    print(f'You harvest {harvest} bushels of grains per acre.')
    print(f'Rats ate {rats} bushels of grains.')
    print(f'Now you have {grain} bushels in the storage.\n')

def final():
    print(f'For the last 10 years {percent_died}% died in average because of starving')
    print(f'Total died - {died_total} people!')
    L = land//population
    print('In the beginning you had 10 acres of land per person')
    print(f'In the end you have {L} acres per person.\n')
    if percent_died > 33 or L < 7:
        endGameBad()
    elif percent_died > 10 or L < 9:
        print('You was a cruel ruler, the remaining people will have you for a long time')
    elif percent_died > 3 or L < 10:
        print(f'You was not bad ruler, however {random.randing(0, int(population * 0.8))} would prefer \nthat your life end as a result of an assassination attempt')
    else:
        print('Fantastic result!')
        print('You are the top-10 world leader, even better that those perfect CEOs from Linkedin')

print('\t\t\t\t Hammurabi Game')
print('\n\n\nTry to rule the ancient country')
print('for 10 years.\n')

year = 0
starved = 0
population = 100
rats = 200
harvest_total = 3000
grain = harvest_total - rats
harvest = 3
land = harvest_total // harvest
people_came = 5
percent_died = 0
died_total = 0

while True:
    year = year + 1
    plague()
    report()
    if year == 11:
        break
    tradeLand()
    feedPeople()
    plantSeeds()
    ratsInvasion()
    harvestGrain()
    changePopulation()
final()
quit()


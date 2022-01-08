import json
from random import randint 

world_map = [['H/T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]


print("Welcome to Ratventure!")
print("----------------------")

# Rat Stats
rat_damage = [1,3]
rat_defence =  1
rat_health = 10

# Hero Stats
hero_name = input('Please enter your hero name: ')
hero_health = 20
hero_damage = [2,4]
hero_defence = 1
d = '2 - 4'

# King Stats
king_health = 25
king_damage = [6,10]
king_defence = 5

# FUNCTIONS #

# HERO COORDINATES #
# This code is to find the coordinates of the hero during the whole game so that the coordinates can be used in future functions to check its location #
hero_y = 0
hero_x = 0
for sublist in world_map:
    for element in sublist:
        if element == 'H/T':
            hero_x = sublist.index(element)
            hero_y = world_map.index(sublist)

        elif element == 'H':
            hero_x = sublist.index(element)
            hero_y = world_map.index(sublist)

        elif element == 'H/K':
            hero_x = sublist.index(element)
            hero_y = world_map.index(sublist)

# DAY COUNT #
# This function is used to increment a day whenever this function is called back in the game. To show the location of the hero as well, it checks for the hero location as seen # 
# below on the map. #
day = 0
daysentence = ' '

def days():
    global day
    global daysentence
    for sublist in world_map:
        for element in sublist:
            if element == 'H/T':
                result = 'You are in a town.'

            elif element == 'H':
                result = 'You are outdoors.'

            elif element == 'H/K':
                result = 'You see the Rat King!'
    
    day += 1
    daysentence = ('Day {}: {}'.format(day,result))

# MAP #
# This function uses the world map provided in a list and converts it into an actual map. #
def map():
    mapgrid = '' 
    for sublist in world_map:
        mapgrid += '+---+---+---+---+---+---+---+---+\n'
        for element in sublist:
            mapgrid += '|{:^3}'.format(element)
        mapgrid += '|\n'
    mapgrid += '+---+---+---+---+---+---+---+---+'
    return(mapgrid)

# 1.2  #
# RESUME GAME #
# Resume game is similar to the code above, just that this uses dictionary and therefore, the data which is the value needs to be assigned back into the values of the keys in the #
# dictionary. #
def resume():
    global hero_health, hero_damage, hero_defence, day, daysentence, world_map, hero_x, hero_y, orb_x, orb_y
    try: 
        savefile = open('RatventureGame.json','r')
        raw_data = savefile.read()
        saved_data = json.loads(raw_data)
        hero_health = saved_data['Health']
        hero_damage = saved_data['Damage']
        hero_defence = saved_data['Defence']
        world_map = saved_data['Map']
        day = saved_data['Day'] - 1
        daysentence = saved_data['Daysentence']
        hero_x = saved_data['Hero x']
        hero_y = saved_data['Hero y']
        orb_x = saved_data['Orb x']
        orb_y = saved_data['Orb y']
        savefile.close()
    
    except:
        print('There is no data of a previously saved game!')

# 2.1 Show Statistics #
# Used dictionary and for loop to print out the statistics of the hero. #
hero_dict = {'Name': hero_name,'Damage': d,'Defence': hero_defence,'Health': hero_health}
def showstats():
    for key,value in hero_dict.items():
        print('{}: {}'.format(key,value))

# 2.3 Moving #
def movemap():
    mapgrid = '' 
    for sublist in world_map:
        mapgrid += '+---+---+---+---+---+---+---+---+\n'
        for element in sublist:
            mapgrid += '|{:^3}'.format(element)
        mapgrid += '|\n'
    mapgrid += '+---+---+---+---+---+---+---+---+'

# 4 functions, all check for hero's location to ensure that the hero cannot move out of the world map as the index might be out of range when the hero moves, then removes the 'H' #
# from the square before moving. #
def moveup():
    global hero_y
    global hero_x
    if hero_y > 0:
        if world_map[hero_y][hero_x] == 'H/T':
            world_map[hero_y][hero_x] = 'T'

        elif world_map[hero_y][hero_x] == 'H':
            world_map[hero_y][hero_x] = ' '

        elif world_map[hero_y][hero_x] == 'H/K':
            world_map[hero_y][hero_x] = 'K'

        hero_y -= 1

        if world_map[hero_y][hero_x] == 'T':
            world_map[hero_y][hero_x] = 'H/T'

        elif world_map[hero_y][hero_x] == ' ':
            world_map[hero_y][hero_x] = 'H'

        elif world_map[hero_y][hero_x] == 'K':
            world_map[hero_y][hero_x] = 'H/K'
        
    movemap()
    days()

def movedown():
    global hero_y
    global hero_x
    if hero_y < 7:
        if world_map[hero_y][hero_x] == 'H/T':
            world_map[hero_y][hero_x] = 'T'

        elif world_map[hero_y][hero_x] == 'H':
            world_map[hero_y][hero_x] = ' '

        elif world_map[hero_y][hero_x] == 'H/K':
            world_map[hero_y][hero_x] = 'K'
            
        hero_y += 1

        if world_map[hero_y][hero_x] == 'T':
            world_map[hero_y][hero_x] = 'H/T'

        elif world_map[hero_y][hero_x] == ' ':
            world_map[hero_y][hero_x] = 'H'

        elif world_map[hero_y][hero_x] == 'K':
            world_map[hero_y][hero_x] = 'H/K'

    movemap()
    days()

def moveleft():
    global hero_y
    global hero_x
    if hero_x > 0:
        if world_map[hero_y][hero_x] == 'H/T':
            world_map[hero_y][hero_x] = 'T'

        elif world_map[hero_y][hero_x] == 'H':
            world_map[hero_y][hero_x] = ' '

        elif world_map[hero_y][hero_x] == 'H/K':
            world_map[hero_y][hero_x] = 'K'

        hero_x -= 1

        if world_map[hero_y][hero_x] == 'T':
            world_map[hero_y][hero_x] = 'H/T'

        elif world_map[hero_y][hero_x] == ' ':
            world_map[hero_y][hero_x] = 'H'           

        elif world_map[hero_y][hero_x] == 'K':
            world_map[hero_y][hero_x] = 'H/K'
    
    movemap()
    days()
    
def moveright():
    global hero_y
    global hero_x
    global world_map
    if hero_x < 7:
        if world_map[hero_y][hero_x] == 'H/T':
            world_map[hero_y][hero_x] = 'T'

        elif world_map[hero_y][hero_x] == 'H':
            world_map[hero_y][hero_x] = ' '

        elif world_map[hero_y][hero_x] == 'H/K':
            world_map[hero_y][hero_x] = 'K'
            
        hero_x += 1

        if world_map[hero_y][hero_x] == 'T':
            world_map[hero_y][hero_x] = 'H/T'

        elif world_map[hero_y][hero_x] == ' ':
            world_map[hero_y][hero_x] = 'H'

        elif world_map[hero_y][hero_x] == 'K':
            world_map[hero_y][hero_x] = 'H/K'
    
    movemap()
    days()

# 2.5 #
# Saving the game #
# The dictionary which contains all the information needed to resume the game, is stored in a dictionary and then stored in a file and closed so that it can be opened and #
# read when the resume game is loaded. #
def save():
    saved_data = {'Health': hero_health, 'Damage': hero_damage, 'Defence': hero_defence, 'Map': world_map, 'Day': day, 'Daysentence': daysentence, 'Hero x': hero_x, 'Hero y': hero_y, 'Orb x': orb_x, 'Orb y': orb_y}
    savefile = open('RatventureGame.json', 'w')
    savefile.write(json.dumps(saved_data))
    savefile.close()                                  

# 3
# Enemy Stats #
# This is just to print out the enemy stats by checking the location of the hero, then printing out the correct entity's statistics. #
def enemy_stats():
    if world_map[hero_y][hero_x] == 'H':
        print('''
Encounter! - Rat
Damage: 1 - 3
Defence = 1
HP: {}'''.format(rat_health))

    elif world_map[hero_y][hero_x] == 'H/K':
        print('''
Encounter! - Rat King
Damage: 6 - 10
Defence: 5
HP: {}'''.format(king_health))

# Combat menu #
# This function is used to generate a random number between 0 and 100 and used to randomly generate a rat attack which is a 50% chance of happening. #
def combat():
    global rat_health, king_health, hero_health
    chance = randint(0,100)
    
    if 50 > chance and world_map[hero_y][hero_x] != 'H/T':
        rat_health = 10
        print('{}'.format(daysentence))
        enemy_stats()
        showcombatchoice()

    elif world_map[hero_y][hero_x] == 'H/K':
        king_health = 25
        print('{}'.format(daysentence))
        enemy_stats()
        showcombatchoice()
    
    else:
        check()

# This is just to print out the choices and checks the input and calls back the appropriate function. #
def showcombatchoice():
    print('''
1) Attack
2) Run''')
    combatchoice = int(input('Enter choice: '))
    if combatchoice == 1:
        attack()

    elif combatchoice == 2:
        run()

# 3.1 #
# Attack #
# This function is to attack and the steps to deduct the entity's health and generate the entity's damage dealt. #
hero_alive = True
king_alive = True
def attack():
    global rat_damage, rat_health, rat_defence, hero_damage, hero_health, hero_defence, king_damage, king_health, king_defence, hero_alive, king_alive
    if world_map[hero_y][hero_x] == 'H/K':
        hdmg = randint(hero_damage[0], hero_damage[1]) - king_defence
        kdmg = randint(king_damage[0], king_damage[1]) - hero_defence
        if hdmg <= 0:
            hdmg = 0
        
        if kdmg <= 0:
            kdmg = 0
        print('You deal {} damage to the Rat King'.format(hdmg))
        print('Ouch! The Rat King hit you for {} damage'.format(kdmg))

        king_health = king_health - hdmg 
        hero_health = hero_health - kdmg
        if king_health <= 0:
            king_health = 0
        
        if hero_health <= 0:
            hero_health = 0

        print('You have {} HP left'.format(hero_health))

        if king_health <= 0:
            print('You have defeated the Rat King! You win the game!')
            leaderboard_list.append([hero_name,day])
            savingleaderboard()
            king_alive = False
            exit()

        elif hero_health <= 0:
            print('Game Over. You have been defeated!')
            hero_alive = False
            exit()

        else:
            enemy_stats()
            showcombatchoice()

    else:
        hdmg = randint(hero_damage[0], hero_damage[1]) - rat_defence
        rdmg = randint(rat_damage[0], rat_damage[1]) - hero_dict['Defence']
        if hdmg <= 0:
            hdmg = 0
        
        if rdmg <= 0:
            kdmg = 0
        
        print('You deal {} damage to the Rat'.format(hdmg))
        print('Ouch! The Rat hit you for {} damage'.format(rdmg))

        rat_health = rat_health - hdmg 
        hero_health = hero_health - rdmg 
        if rat_health <= 0:
            rat_health = 0
        
        if hero_health <= 0:
            hero_health =0
        
        print('You have {} HP left'.format(hero_health))
        
        if rat_health <= 0:
            print('You have defeated the Rat!')
            hero_dict['Health'] = hero_health
            check()

        elif hero_health <= 0:
            print('Game Over. You have been defeated!')
            hero_alive = False
            exit()
            

        else:
            enemy_stats()
            showcombatchoice()

# 3.2 #
# This is to reset the rat health and shows the outdoor menu when the player selects run #
def run():
    rat_health = 10
    showoutdoormenu()

# 4.4 #
# Sense Orb #
# This function is used to sense the randomized location of the orb compared with the hero coordinates. #
def sense_orb():
    global direction, orb_x, orb_y, hero_x, hero_y,hero_damage,hero_dict,d,hero_defence
    direction = ''
    if orb_y < hero_y:
        direction += 'North'

    elif orb_y > hero_y:
        direction += 'South'

    if orb_x < hero_x:
        direction += 'West'

    elif orb_x > hero_x:
        direction += 'East'
    
    if world_map[hero_y][hero_x] == world_map[orb_y][orb_x]:
        print('''
You have found the Orb Of Power!
Your attack increases by 5!
Your defence increases by 5!''')
        hero_damage = [5,9]
        hero_defence = 6
        d = '7 - 9'
        hero_dict['Damage'] = d
        hero_dict['Defence'] = 6
    else:
        print('You sense that the Orb of Power is {}'.format(direction))
    
    days()

# Advanced Requirements #

# RANDOMIZING TOWNS #
# This function randomizes the towns by giving random coordinates to the towns at first, then checking for the location of each town to ensure that they are all at least 3 steps #
# away from each other. #
def randomizetown():
    global world_map
    counter = 0
    world_map = [['H/T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
    while True:
            townplace = True
            town_x = randint(0,7)
            town_y = randint(0,7)
            
            for x in range(-2, 3):
                starting_y = abs(x) - 2
                ending_y = abs(starting_y)
                for y in range(starting_y,ending_y + 1):
                    if (x + town_x) > 7 or (x + town_x) < 0 or (y + town_y) > 7 or (y + town_y) < 0: 
                        continue 
                    
                    if world_map[y + town_y][x + town_x] != ' ' or world_map[y + town_y][x + town_x] == 'K':
                        townplace = False

            if townplace == True:
                world_map[town_y][town_x] = 'T'
                counter += 1
            if counter == 4:
                break


# RANDOMIZE LOCATION OF ORB #
# This function is to randomize the location of the orb whenever a new game is run. It is done by assigning random coordinates to the orb. Once this is done, it needs to be checked #
# because the orb cannot be placed in a town, with the rat king, or within the first 4 rows and columns. #
orb_y = 0
orb_x = 0

def randomize_orb():
    Placeable = True
    global orb_x, orb_y
    while Placeable == True:
        orb_x = randint(0,7)
        orb_y = randint(0,7)
        if orb_x < 4 or orb_y < 4 and world_map[orb_y][orb_x] != ' ':
            Placeable = True

        else:
            break

# LEADERBOARD #
# This function is to create a list for the leaderboard so that once the hero wins, the hero name and day number will be appended in a nested list to the leaderboard list. #
# To save it, a json file is created and opened to edit/write and the data is stored and saved in the file. Once that is done, the file is closed for safety. #
leaderboard_list = []
def savingleaderboard():
    leaderboardfile = open('Leaderboard.json', 'w')
    leaderboardfile.write(json.dumps(leaderboard_list))
    leaderboardfile.close()

# This function is to display the leaderboard when the function is called in option 4 in the main menu. The function opens and reads the file and uses a for loop to print out the #
# data inside. A counter is used to show the ranking of the leaderboard. #
def loadingleaderboard():
    try:
        leaderboardfile = open('Leaderboard.json', 'r')
        leaderboard_data = leaderboardfile.read()
        leaderboard_list = json.loads(leaderboard_data)
        counter = 0
        print('# LeaderBoard Ranking #')
        for sublist in leaderboard_list:
            leaderboard_list.sort(key = lambda x : x[1])
            counter += 1
            print('{}. {} took {} days to defeat the Rat King'.format(counter,sublist[0],sublist[1]))
        leaderboardfile.close()
    
    except:
        print('Currently, no one has defeated the Rat King! Be the first one to do so!')

# Printing out different menus #
def showmenu():
    print('''
1) New Game
2) Resume Game
3) Exit Game
4) View Leaderboard''')

def showtownmenu():
    print('''
{}
1) View Character
2) View Map
3) Move
4) Rest
5) Save Game
6) Exit Game
'''.format(daysentence))

def showoutdoormenu():
    print('''
{}
1) View Character
2) View Map
3) Move
4) Sense Orb
5) Exit Game'''.format(daysentence))

# Checking for location of hero to display correct menus and input #
def check():
    if world_map[hero_y][hero_x] == 'H/T':
        showtownmenu()
        town()

    elif world_map[hero_y][hero_x] == 'H':
        showoutdoormenu()
        outdoor()

# Town choice loop #
# Runs when location of hero is in a town. #
townthingy = True
movethingy = True
def town():
    global hero_health,townthingy,movethingy,king_alive,hero_alive
    while townthingy == True:
        if world_map[hero_y][hero_x] == 'H':
            outdoor()
            break
        
        if king_alive == False or hero_alive == False:
            break

        else:
            townchoice = input('Enter town choice: ')
            if townchoice.isdigit() and 0 < int(townchoice) < 7:    # Checks input whether it is a digit and between 1 amd 7
                townchoice = int(townchoice)

                if townchoice == 1:
                    showstats()
                    check()

                elif townchoice == 2:
                    print(map())
                    check()

                elif townchoice == 3:
                    while movethingy == True:            # Runs until it does not return True for input validation. #
                        movechoice = input('Use WASD to move: ')        # Checks whether input is WASD #
                        if movechoice == 'W' or movechoice == 'A' or movechoice == 'S' or movechoice == 'D':
                            if movechoice == 'W':
                                moveup()
                                print(map())
                                combat()
                                if hero_alive == False:
                                    break
                                elif king_alive == False:
                                    break
                                break

                            elif movechoice == 'A':
                                moveleft()
                                print(map())
                                combat()
                                if hero_alive == False:
                                    break
                                elif king_alive == False:
                                    break
                                break

                            elif movechoice == 'D':
                                moveright()
                                print(map())
                                combat()
                                if hero_alive == False:
                                    break
                                elif king_alive == False:
                                    break
                                break

                            elif movechoice == 'S':
                                movedown()
                                print(map())
                                combat()
                                if hero_alive == False:
                                    break
                                elif king_alive == False:
                                    break
                                break
                            
                        else:
                            print('Error! Please try to move again!')   # Error shows up when the input is not WASD #
                            movethingy = True

                elif townchoice == 4:
                    hero_dict['Health'] = 20
                    print('You are fully healed!')
                    days()
                    check()
                    

                elif townchoice == 5:
                    save()
                    print('Your game has been saved.')
                    exit()

                elif townchoice == 6:
                    print('You have exited the game!')
                    exit()
        
            else:
                print('Error! Please try entering a number again')   # Error shows up when the input is not a number or out of range #
                townthingy = True
                showtownmenu()

# Outdoor Choice Loop #
# Runs when the location of hero is outdoors and not in a town. #
outdoorthingy = True
movethingy = True
def outdoor():
    global outdoorthingy,movethingy,king_alive,hero_alive
    while outdoorthingy == True:
        if world_map[hero_y][hero_x] == 'H/T':
            town()
            break
        
        if king_alive == False or hero_alive == False:
            break

        else:
            outdoorchoice = input('Enter outdoor choice: ')
            if outdoorchoice.isdigit() and 0 < int(outdoorchoice) < 6:
                outdoorchoice = int(outdoorchoice)
                if outdoorchoice == 1:
                    showstats()
                    check()

                elif outdoorchoice == 2:
                    print(map())
                    check()

                elif outdoorchoice == 3:
                    while movethingy == True:            # Runs until it does not return True for input validation. #
                        movechoice = input('Use WASD to move: ')     # Checks whether input is WASD #
                        if movechoice == 'W' or movechoice == 'A' or movechoice == 'S' or movechoice == 'D':
                            if movechoice == 'W':
                                moveup()
                                print(map())
                                combat()
                                if hero_alive == False:
                                    break
                                elif king_alive == False:
                                    break
                                break

                            elif movechoice == 'A':
                                moveleft()
                                print(map())
                                combat()
                                if hero_alive == False:
                                    break
                                elif king_alive == False:
                                    break
                                break

                            elif movechoice == 'D':
                                moveright()
                                print(map())
                                combat()
                                if hero_alive == False:
                                    break
                                elif king_alive == False:
                                    break
                                break

                            elif movechoice == 'S':
                                movedown()
                                print(map())
                                combat()
                                if hero_alive == False:
                                    break
                                elif king_alive == False:
                                    break
                                break
                            
                        else:
                            print('Error! Please try to move again!')   # Error shows up when the input is not WASD #
                            movethingy = True
                        
                elif outdoorchoice == 4:
                    sense_orb()
                    check()

                elif outdoorchoice == 5:
                    print('You have exited the game.')
                    exit()
            
            else:
                print('Error! Please try entering a number again')   # Error that shows up when there is a wrong input #
                outdoorthingy = True
                showoutdoormenu()
showmenu()
# Menu Choice #
menu = True
while menu == True:
    startchoice = input('Enter menu choice: ')
    if startchoice.isdigit() and 0 < int(startchoice) < 5:  # Input validation #
        startchoice = int(startchoice)
        if startchoice == 1:
            hero_alive = True
            king_alive = True
            day = 0
            randomizetown()
            randomize_orb()
            days()
            check()

        elif startchoice == 2:
            print('You have loaded your saved game!')  # Resets the booleans #
            hero_alive = True
            king_alive = True
            resume()
            check()

        elif startchoice == 3:
            break
        
        elif startchoice == 4:
            loadingleaderboard()
            showmenu()

    else:
        print('Error! Please try entering a number again') # Error that shows up when the input is incorret. #
        menu = True
        showmenu()
        

        
                    
    


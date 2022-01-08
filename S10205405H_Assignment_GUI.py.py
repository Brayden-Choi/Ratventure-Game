import json
from random import randint  
from tkinter import messagebox
from tkinter import *
window = Tk()

# +------------------------
# | Text for various menus 
# +------------------------
main_text = ["New Game",\
             "Resume Game",\
#             "View Leaderboard",\
             "Exit Game"]

town_text = ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game"]

open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]

fight_text = ["Attack",\
              "Run"]

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

#Start
# Rat Stats
rat_damage = [1,3]
rat_defence =  1
rat_health = 10

# Hero Stats
hero_health = 20
hero_damage = [10,15]
hero_defence = 20

# King Stats
king_health = 25
king_damage = [8,12]
king_defence = 5

#Showing the Day Count
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
    dayLabel.configure(text = daysentence)
    rundayLabel.configure(text = daysentence)
    combatdayLabel.configure(text = daysentence)

#Resume Game
def resume():
    global health
    global damage
    global defense
    global day
    global daysentence
    global world_map
    global hero_x
    global hero_y
    savefile = open('RatventureGame.json','r')
    raw_data = savefile.read()
    saved_data = json.loads(raw_data)
    health = saved_data['Health']
    damage = saved_data['Damage']
    defense = saved_data['Defence']
    world_map = saved_data['Map']
    day = saved_data['Day'] - 1
    daysentence = saved_data['Daysentence']
    hero_x = saved_data['X-coordinates']
    hero_y = saved_data['Y-coordinates']
    savefile.close()
    restshow_new()

#Exit Game
def exit():
    messagebox.showinfo(title='Ratventure Message', message='You Have Exited The Game.')
    window.destroy()
    
#2.1
def showstats():
    newFrame.place_forget()
    op1Frame.place(x=0,y=0)
    op2Frame.place_forget()
    op3Frame.place_forget()
    op4Frame.place_forget()
    combatFrame.place_forget()
    attackFrame.place_forget()
    runFrame.place_forget()
    senseorbFrame.place_forget()
    attackFrame.place_forget()
    new4Title.configure(text = 'HP: {}'.format(hero_health))

def runshowstats():
    newFrame.place_forget()
    op1Frame.place(x=0,y=0)
    op2Frame.place_forget()
    op3Frame.place_forget()
    op4Frame.place_forget()
    combatFrame.place_forget()
    attackFrame.place_forget()
    runFrame.place_forget()
    senseorbFrame.place_forget()
    attackFrame.place_forget()

#2.2
def map():
    mapgrid = '' 
    for sublist in world_map:
        mapgrid += '+---+---+---+---+---+---+---+---+\n'
        for element in sublist:
            mapgrid += '|{:^3}'.format(element)
        mapgrid += '|\n'
    mapgrid += '+---+---+---+---+---+---+---+---+'

    mapText.configure(state = 'normal')
    mapText.delete('1.0', 'end')
    mapText.insert('end', mapgrid)
    mapText.configure(state = 'disabled')

    newFrame.place_forget()
    op1Frame.place_forget()
    op2Frame.place(x=0,y=0)
    op3Frame.place_forget()
    op4Frame.place_forget()
    runFrame.place_forget()
    combatFrame.place_forget()
    senseorbFrame.place_forget()
    attackFrame.place_forget()

#2.3
def movemap():
    mapgrid = '' 
    for sublist in world_map:
        mapgrid += '+---+---+---+---+---+---+---+---+\n'
        for element in sublist:
            mapgrid += '|{:^3}'.format(element)
        mapgrid += '|\n'
    mapgrid += '+---+---+---+---+---+---+---+---+'

    newmapText.configure(state = 'normal')
    newmapText.delete('1.0', 'end')
    newmapText.insert('end', mapgrid)
    newmapText.configure(state = 'disabled')

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
    backcheck()
    combat()
    

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
    backcheck()
    combat()
    

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
    backcheck()
    combat()

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
    backcheck()
    combat()
    

def move():
    if hero_y == 0:
        upButton.configure(state = 'disabled')
    else:
        upButton.configure(state = 'normal')
    
    if hero_y == 7:
        downButton.configure(state = 'disabled')
    else:
        downButton.configure(state = 'normal')
    
    if hero_x == 0:
        leftButton.configure(state = 'disabled')
    else:
        leftButton.configure(state = 'normal')
    
    if hero_x == 7:
        rightButton.configure(state = 'disabled')
    else:
        rightButton.configure(state = 'normal')

    newFrame.place_forget()
    op1Frame.place_forget()
    op2Frame.place_forget()
    op3Frame.place(x=0,y=0)
    op4Frame.place_forget()
    runFrame.place_forget()
    combatFrame.place_forget()
    movemap()
    senseorbFrame.place_forget()
    attackFrame.place_forget()

#2.4
def rest():
    global hero_health
    hero_health = 20
    newFrame.place_forget()
    op1Frame.place_forget()
    op2Frame.place_forget()
    op4Frame.place(x=0,y=0)
    combatFrame.place_forget()

#2.5
#Save the game
def save():
    data = {'Health': hero_health, 'Damage': hero_damage, 'Defence': hero_defence, 'Map': world_map, 'Day': day, 'Daysentence': daysentence, 'X-coordinates': hero_x, 'Y-coordinates': hero_y}
    savefile = open('RatventureGame.json', 'w')
    savefile.write(json.dumps(data))
    savefile.close()
    messagebox.showinfo(title='Ratventure Message', message='Your Game Has Been Saved')
    menuFrame.place(x=0,y=0)                                  

# 3
# Combat menu
def combat():
    global rat_health
    chance = randint(0,100)
    if 0 > chance and world_map[hero_y][hero_x] != 'H/T':
        rat_health = 10
        ratstats1Title.place(x=550,y=300)
        ratstats2Title.place(x=550,y=400)
        kingstats1Title.place_forget()
        kingstats2Title.place_forget()
        show_combat()
    
    if world_map[hero_y][hero_x] == 'H/K':
        kingstats1Title.place(x=550,y=300)
        kingstats2Title.place(x=550,y=400)
        ratstats1Title.place_forget()
        ratstats2Title.place_forget()
        show_combat()
        
        
        
# 3.1
# Attack 
def attack():
    global rat_damage, rat_health, rat_defence, hero_damage, hero_health, hero_defence, king_damage, king_health, king_defence
    attackButton.place(x=450,y=600)
    runButton.place(x=1000,y=600)
    herowinTitle.place_forget()
    continueButton.place_forget()
    
    if world_map[hero_y][hero_x] == 'H/K':
        hdmg = randint(hero_damage[0], hero_damage[1]) - king_defence
        kdmg = randint(king_damage[0], king_damage[1]) - hero_defence
        if hdmg <= 0:
            hdmg = 0
        
        if kdmg <= 0:
            kdmg = 0

        king_health = king_health - hdmg 
        hero_health = hero_health - kdmg
        if king_health <= 0:
            king_health = 0
        
        if hero_health <= 0:
            hero_health =0
        herodmgTitle.configure(text = 'You attacked the King for {} damage'.format(hdmg))
        kingdmgTitle.configure(text = 'The King attacked you for {} damage'.format(kdmg))
        herohealthTitle.configure(text = 'You have {} HP left'.format(hero_health))
        kinghealthTitle.configure(text = 'The King has {} HP left'.format(king_health))
        herodmgTitle.place(x=500,y=200)
        kingdmgTitle.place(x=500,y=300)
        herohealthTitle.place(x=500,y=400)
        kinghealthTitle.place(x=500,y=500)

    else:
        hdmg = randint(hero_damage[0], hero_damage[1]) - rat_defence
        rdmg = randint(rat_damage[0], rat_damage[1]) - hero_defence
        if hdmg <= 0:
            hdmg = 0
        
        if rdmg <= 0:
            kdmg = 0
        rat_health = rat_health - hdmg 
        hero_health = hero_health - rdmg 
        if rat_health <= 0:
            rat_health = 0
        
        if hero_health <= 0:
            hero_health =0
        herodmgTitle.configure(text = 'You attacked the rat for {} damage'.format(hdmg))
        ratdmgTitle.configure(text = 'The rat attacked you for {} damage'.format(rdmg))
        herohealthTitle.configure(text = 'You have {} HP left'.format(hero_health))
        rathealthTitle.configure(text = 'The rat has {} HP left'.format(rat_health))
        herodmgTitle.place(x=500,y=200)
        ratdmgTitle.place(x=500,y=300)
        herohealthTitle.place(x=500,y=400)
        rathealthTitle.place(x=500,y=500)

    if rat_health <= 0 or king_health <=0:
        herowinTitle.place(x=500,y=800)
        continueButton.place(x=600,y=900)
        attackButton.place_forget()
        runButton.place_forget()

    if hero_health <= 0:
        ratwinTitle.place(x=500,y=800)
        returnButton.place(x=600,y=900)
        attackButton.place_forget()
        runButton.place_forget()

    attackFrame.place(x=0,y=0)

# 3.2
# Run
def run():
    rat_health = 10
    runFrame.place(x=0,y=0)
    
# 4.4
# Randomizing the Orb
orb_y = 0
orb_x = 0

def randomize_orb():
    Placeable = True
    global orb_x, orb_y
    while True:
        orb_x = randint(0,7)
        orb_y = randint(0,7)
        if orb_x < 4 or orb_y < 4 and world_map[orb_y][orb_x] != ' ':
            Placeable = False

        else:
            break
        
# Sense Orb
def sense_orb():
    global direction, orb_x, orb_y, hero_x, hero_y,hero_damage,hero_defence
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
        senseTitle.configure(text = '''
You have found the Orb Of Power!
Your attack increases by 5!
Your defence increases by 5!''')
        hero_damage = [2,9]
        hero_defence = 6
        new2Title.configure(text = 'Damage:2 to 9')
        new3Title.configure(text = 'Defence: 7')
    else:
        senseTitle.configure(text = 'The Direction of the Orb is {}'.format(direction))
    
    combatFrame.place_forget()
    runFrame.place_forget()
    attackFrame.place_forget()
    senseorbFrame.place(x=0,y=0)
    days()

# Randomize Town
def randomizetown():
    counter = 0
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

# LEADERBOARD #
leaderboard_list = []
def savingleaderboard():
    leaderboardfile = open('Leaderboard.json', 'w')
    leaderboardfile.write(json.dumps(leaderboard_list))
    leaderboardfile.close()

def loadingleaderboard():
    try:
        ldsentence = ''
        leaderboardfile = open('Leaderboard.json', 'r')
        leaderboard_data = leaderboardfile.read()
        leaderboard_list = json.loads(leaderboard_data)

    except:
        menuFrame.place_forget()
        runFrame.place_forget()
        newFrame.place_forget()
        op3Frame.place_forget()
        ldFrame.place(x=0,y=0)
        ldTitle.place(x=400,y=200)
    
    else:
        counter = 0
        ldsentence = '# LeaderBoard Ranking #\n'
        for sublist in leaderboard_list:
            leaderboard_list.sort(key = lambda x : x[1])
            counter += 1
            ldsentence += '{}. {} took {} days to defeat the Rat King'.format(counter,sublist[0],sublist[1])
        leaderboardfile.close()
        ldText.configure(state = 'normal')
        ldText.delete('1.0', 'end')
        ldText.insert('end', ldsentence)
        ldText.configure(state = 'disabled')
        ldTitle.place_forget()
        menuFrame.place_forget()
        runFrame.place_forget()
        newFrame.place_forget()
        op3Frame.place_forget()
        ldFrame.place(x=0,y=0)

#GUI
def show_new():
    combatFrame.place_forget()
    attackFrame.place_forget()
    runFrame.place_forget()
    menuFrame.place_forget()
    newFrame.place(x=0,y=0)
    
def modifiedshow_new():
    global day, health, damage, defense, world_map
    randomize_orb()
    menuFrame.place_forget()
    newFrame.place(x=0,y=0)
    health = 20
    damage = [2,4]
    defence = 1
    day = 0
    world_map = [['H/T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
    days()
    randomizetown()

def restshow_new():
    menuFrame.place_forget()
    combatFrame.place_forget()
    attackFrame.place_forget()
    runFrame.place_forget()
    newFrame.place(x=0,y=0)
    days()

def show_menu():
    combatFrame.place_forget()
    attackFrame.place_forget()
    runFrame.place_forget()
    menuFrame.place(x=0,y=0)

def show_combat():
    combatFrame.place(x=0,y=0)
    newFrame.place_forget()
    runFrame.place_forget()

def backcheck():
    if world_map[hero_y][hero_x] == 'H/T':
        newFrame.place(x=0,y=0)
        op1Frame.place_forget()

    else:
        runFrame.place(x=0,y=0)    
        op1Frame.place_forget()

# Leaderboard Frame
ldFrame = Frame(window,bg = 'light cyan',width = 1920, height = 1080)

ldText = Text(ldFrame,bg = 'light cyan',height = 1920, width = 1080, font = ('Arial',20))
ldTitle = Label(ldFrame, text = 'Currently,no one has defeated the Rat King. Be the first one to do so!', font = ('Arial',30))
button = Button(ldFrame,text = 'Back to main menu', width = 17, command = show_menu,  font = ('Arial',20) )
ldText.place(x=400,y=100)
button.place(x=1400,y=700)

#option 1 frame
op1Frame = Frame(window, bg = 'light cyan',width = 1920, height = 1080)

new1Title = Label(op1Frame,text = 'Name: The Hero',width = 14,font=('Arial',40))
new2Title = Label(op1Frame,text = 'Damage: 2 to 4',width = 14,font=('Arial',40))
new3Title = Label(op1Frame,text = 'Defence: 1',width = 14,font=('Arial',40))
new4Title = Label(op1Frame,text = 'HP: 20',width = 14,font=('Arial',40))
backButton = Button(op1Frame,text = 'Back',width = 14, command = backcheck,font = ('Arial',30))

new1Title.place(x=800,y=200)
new2Title.place(x=800,y=400)
new3Title.place(x=800,y=600)
new4Title.place(x=800,y=800)
backButton.place(x=150,y=800)


#option 2 frame
op2Frame = Frame(window, bg = 'light cyan',width = 1920, height = 1080)

mapText = Text(op2Frame,bg = 'light cyan',height = 1920, width = 1080, font = ('Monaco',30))
backButton = Button(op2Frame,text = 'Back',width = 4, command = backcheck,font = ('Arial',30))
mapText.place(x=500,y=200)
backButton.place(x=150,y=800)

#option 3 frame
op3Frame = Frame(window, bg = 'light cyan',width = 1920, height = 1080)

upButton = Button(op3Frame,text = 'UP',width = 10,command = moveup,font = ('Arial',15))
downButton = Button(op3Frame,text = 'DOWN',width = 10,command = movedown,font = ('Arial',15))
leftButton = Button(op3Frame,text = 'LEFT',width = 10, command = moveleft,font = ('Arial',15))
rightButton = Button(op3Frame,text = 'RIGHT',width = 10,command = moveright, font = ('Arial',15))
newmapText = Text(op3Frame,bg = 'light cyan',height = 1920, width = 1080, font = ('Monaco',30))

upButton.place(x=300,y=750)
downButton.place(x=300,y=800)
leftButton.place(x=150,y=800)
rightButton.place(x=450,y=800)
newmapText.place(x=800,y=100)

#option 4 frame
op4Frame = Frame(window, bg = 'light cyan',width = 1920, height = 1080)

restTitle = Label(op4Frame,text = 'You are fully healed',width = 20,font=('Arial',50))
continueButton = Button(op4Frame,text = 'Continue',width = 8, command = restshow_new,font = ('Arial',30))
restTitle.place(x=600,y=300)
continueButton.place(x=900,y=700)

# Sense Orb Frame
senseorbFrame = Frame(window, bg = 'light cyan',width = 1920, height = 1080)
senseTitle = Label(senseorbFrame,text = '',width = 28,font = ('Arial',30))
nextButton = Button(senseorbFrame,text = 'Next Day',width = 8, command = backcheck ,font = ('Arial',30))
senseTitle.place(x=800,y=300)
nextButton.place(x=1400,y=900)

# Combat Frame GUI
combatFrame = Frame(window,bg = 'light cyan',width = 1920, height = 1080)
ratTitle = Label(combatFrame,text = 'You Have Encountered A Rat! Attack Or Run!?', width = 60,font = ('Arial',30))
ratstats1Title = Label(combatFrame,text = 'Rat Damage = 1-3',width = 60,font=('Arial',20))
ratstats2Title = Label(combatFrame,text = 'Rat HP: 10',width = 60,font=('Arial',20))
kingstats1Title = Label(combatFrame,text = 'King Damage = 8-12',width = 60,font=('Arial',20))
kingstats2Title = Label(combatFrame,text = 'King HP: 25',width = 60,font=('Arial',20))
attackButton = Button(combatFrame,text = 'Attack',width = 20,command = attack,font = ('Arial',30))
runButton = Button(combatFrame,text = 'Run',width = 20,command = run, font = ('Arial',30))
ratTitle.place(x=300,y=200)
attackButton.place(x=750,y=500)
runButton.place(x=750,y=700)
ratstats1Title.place(x=550,y=300)
ratstats2Title.place(x=550,y=400)

combatdayLabel = Label(combatFrame, text = daysentence,width = 40,font = ('Arial',30))
combatdayLabel.place(x=600,y=50)

# Attack GUI
attackFrame = Frame(window,bg = 'light cyan',width = 1920, height = 1080)
herodmgTitle = Label(attackFrame,text = '',width = 60,font=('Arial',20))
ratdmgTitle = Label(attackFrame,text = '',width = 60,font=('Arial',20))
kingdmgTitle = Label(attackFrame,text = '',width = 60,font=('Arial',20))
herohealthTitle = Label(attackFrame,text = '',width = 60,font=('Arial',20))
rathealthTitle = Label(attackFrame,text = '',width = 60,font=('Arial',20))
kinghealthTitle = Label(attackFrame,text = '',width = 60,font=('Arial',20))
herowinTitle = Label(attackFrame,text = 'You have defeated the rat! Press Continue to Advance!',width = 60,font=('Arial',20))
ratwinTitle = Label(attackFrame,text = 'You have lost! Game over!',width = 60,font=('Arial',20))
attackButton = Button(attackFrame,text = 'Continue Attacking',width = 30,command = attack, font = ('Arial',20))
runButton = Button(attackFrame,text = 'Run',width = 30,command = backcheck, font = ('Arial',20))
continueButton = Button(attackFrame,text = 'Continue',width = 40,command = backcheck, font = ('Arial',20))
returnButton = Button(attackFrame,text = 'Continue',width = 40,command = show_menu, font = ('Arial',20))

attackButton.place(x=450,y=600)
runButton.place(x=1000,y=600)

# Run GUI
runFrame = Frame(window,bg = 'light cyan',width = 1920, height = 1080)
o1Button = Button(runFrame,text = 'View Character',width = 14,command = showstats, font = ('Arial',30))
o2Button = Button(runFrame,text = 'View Map',width = 14,command = map, font = ('Arial',30))
o3Button = Button(runFrame,text = 'Move',width = 14,command = move, font = ('Arial',30))
o4Button = Button(runFrame,text = 'Sense Orb',width = 14,command = sense_orb, font = ('Arial',30))
o5Button = Button(runFrame,text = 'Exit Game',width = 14,command = show_menu, font = ('Arial',30))
              
o1Button.place(x=800,y=200)
o2Button.place(x=800,y=300)
o3Button.place(x=800,y=400)
o4Button.place(x=800,y=500)
o5Button.place(x=800,y=600)

rundayLabel = Label(runFrame, text = daysentence,width = 40,font = ('Arial',30))
rundayLabel.place(x=600,y=50)

#new game frame
newFrame = Frame(window, bg = 'light cyan',width = 1920, height = 1080)

op1Button = Button(newFrame,text = 'View Character',width = 14,command = showstats, font = ('Arial',30))
op2Button = Button(newFrame,text = 'View Map',width = 14,command = map, font = ('Arial',30))
op3Button = Button(newFrame,text = 'Move',width = 14,command = move, font = ('Arial',30))
op4Button = Button(newFrame,text = 'Rest',width = 14,command = rest, font = ('Arial',30))
op5Button = Button(newFrame,text = 'Save Game',width = 14,command = save, font = ('Arial',30))
op6Button = Button(newFrame,text = 'Exit Game',width = 14,command = show_menu, font = ('Arial',30))                 

op1Button.place(x=800,y=200)
op2Button.place(x=800,y=300)
op3Button.place(x=800,y=400)
op4Button.place(x=800,y=500)
op5Button.place(x=800,y=600)
op6Button.place(x=800,y=700)

dayLabel = Label(newFrame, text = daysentence,width = 40,font = ('Arial',30))
dayLabel.place(x=600,y=50)

#Main Menu
window.title('Ratventure')
window.geometry('1920x1080')
menuFrame = Frame(window,bg='linen',width=1920,height=1080)
menuTitle = Label(menuFrame,text = 'Welcome to Ratventure', width=21, font=('Arial',50))
newButton = Button(menuFrame,text='New Game',width=20,font=('Arial',30),command=modifiedshow_new)
resumeButton = Button(menuFrame,text='Resume Game',width=20,font=('Arial',30),command=resume)
exitButton = Button(menuFrame,text='Exit Game',width=20,font=('Arial',30),command=exit)
ldButton = Button(menuFrame,text='View Leaderboard',width=20,font=('Arial',30),command=loadingleaderboard)
menuFrame.place(x=0,y=0)
menuTitle.place(x=550,y=50)
newButton.place(x=730,y=200)
resumeButton.place(x=730,y=400)
exitButton.place(x=730,y=600)
ldButton.place(x = 730,y=800)
window.mainloop()


    


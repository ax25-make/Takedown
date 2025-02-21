# Final Project
# CS 111, Hayes & Reckinger
# project takedown
# TODO: Comment here

import turtle
import random

#boss gaunlet after each boss goto next #6 bosses randomized order
    
#take images and place their names in a txt and them addshapes to turtle with a loop
def turtle_shapes(filename):
    with open(filename) as raw:
        for asset in raw:
            asset_line = asset.split()
            turtle.addshape(asset_line[0])

#makes dict from cards.txt
def read_data(filename):
    cards = {}
    with open(filename) as raw:
        for line in raw:
            line_cards = line.split()
            cards[line_cards[0]] = int(line_cards[1])
            turtle.addshape(line_cards[0])
    return cards

#general screen setup
def screen_setup(): 
    global screen
    screen = turtle.Screen()
    screen.setup(810, 685, None, 10)
    screen.screensize(800, 675)

#setup for a bunch of variables
def general_setup(): 
    global boss_num
    global rating
    global max_health
    global current_health
    global damage_taken
    global card_counter

    rating =  random.randint(1, 5)
    max_health = 100 * rating
    current_health = max_health
    card_counter = 0

def create_cards(): #draw in cards
    global card_turtle_list
    global cards

    #grabs a random card for the list of dictionary keys
    card = random.choice(list(cards.keys())) 

    #a turtle gets added to a list and has a shape added to it
    card_turtle = turtle.Turtle()
    card_turtle_list.append(card_turtle)

    card_turtle.shape(card)
    
def card_placement():
    turtle.tracer(False)

    for i in range(len(card_turtle_list)):
        x = i * 200

        card_turtle_list[i].penup()
        card_turtle_list[i].hideturtle()
        card_turtle_list[i].goto(-200 + x, -175)
        card_turtle_list[i].showturtle()

    turtle.tracer(True)

def card_functionality(x=0, y=0): 
    global card_turtle_list
    global current_health
    global cards
    global selected_card
    global card_counter
    global counter_global
    global movement

    selected_card = None

    for card in card_turtle_list:
        if card.distance(x, y) < 100: 
            selected_card = card.shape()

    if selected_card == None:
        damage = 0
    else:
        damage = cards[selected_card] 
        update_health(damage)
        counter_global += 1
        card_counter += 1
        if current_health <= 0:
            interlude_screen()

        else: 
            main()

def update_health(damage):
    global max_health
    global current_health

    current_health -= damage

    #make sure health bar doesnt go negative
    damage_taken = max(0, current_health)

    health_bar(damage_taken)

def health_bar(damage_taken): 
    turtle.tracer(False)
    
    background_bar = turtle.Turtle()
    background_bar.penup()
    background_bar.hideturtle()
    background_bar.fillcolor("black")
    background_bar.begin_fill()
    background_bar.goto(-300, 330)
    background_bar.pendown()
    background_bar.forward(600)
    background_bar.right(90)
    background_bar.forward(25)
    background_bar.right(90)
    background_bar.forward(600)
    background_bar.right(90)
    background_bar.forward(25)
    background_bar.end_fill()
    
    #red bar updates
    #global current_health

    health = turtle.Turtle()
    health.hideturtle()
    health.penup()
    health.pencolor("black")
    health.fillcolor("red")
    health.begin_fill()
    health.goto(-300, 330)
    health.pendown()
    health.forward(600 * (damage_taken / max_health))
    health.right(90)
    health.forward(25)
    health.right(90)
    health.goto(-300, 305)
    health.right(90)
    health.forward(25)
    health.end_fill()
    
    turtle.clear()
    turtle.hideturtle()
    turtle.pencolor("white")    
    turtle.penup()
    turtle.goto(0, 305)
    turtle.write(f"{damage_taken} / {max_health}", True, align = "center", font = ("Comicsans", 15, "bold"))
    turtle.tracer(True)

def boss_display():  
    global boss_num

    #turtle.tracer(False)

    # make it bounce around screen in the top
    boss = turtle.Turtle()
    boss.hideturtle()
    boss.shape(f"boss{boss_num}.gif") #drawings for 6 bosses #make it shuffle the boss list and it the same project cant appear
    boss.penup()
    boss.goto(0, 145)
    boss.showturtle()
    
def difficulty_rating(): #rating for projects randomized
    global rating

    turtle.tracer(False)

    for i in range(rating):
        x = 30 * i
        rating_scale = turtle.Turtle()
        rating_scale.hideturtle()
        rating_scale.shape("rating.gif")
        rating_scale.penup()
        rating_scale.goto(-280 + x, -30)
        rating_scale.showturtle()

    turtle.tracer(True)

def play_screen(x=0, y=0): #go back
    turtle.clearscreen()

    #how play
    turtle.tracer(False)

    screen_setup()
    play_button()

    opening = turtle.Turtle()
    opening.hideturtle()
    opening.penup()
    opening.goto(0, 190)
    opening.write(f"WELCOME TO PROJECT TAKEDOWN", align = "center", font = ("Comicsans", 30, "bold"))
    opening.goto(0, 150)
    opening.write(f"Use Action cards to take down the project!", align = "center", font = ("Comicsans", 24, "normal"))
    opening.goto(0, 110)
    opening.write(f"Aim to use as few Actions as possible for the highest grade", align = "center", font = ("Comicsans", 19, "normal"))

    turtle.tracer(True)

def interlude_screen(x=0, y=0):
    global boss_count
    turtle.clearscreen()

    #game progress
    score()
    
    turtle.tracer(False)

    screen_setup()
    
    #uses next instead of retry depending on whether the project was completed or not
    if boss_count < 6 and attempt == "Completed":
        next_button()

    elif boss_count < 6:
        retry_button()
    
    end_button() 

    turtle.tracer(True)

def end_screen(x=0, y=0): 
    global boss_count
    global card_counter
    turtle.clearscreen()
    turtle.tracer(False)

    final = turtle.Turtle()
    final.hideturtle()
    final.penup()
    final.goto(0, 100)
    if boss_count > 0:
        final.write(f"You have completed {boss_count} project(s)", align = "center", font = ("Comicsans", 30, "bold"))
    else:
        final.write(f"You have completed nothing", align = "center", font = ("Comicsans", 30, "bold"))
    final.goto(0, -150)
    final.write(f"Play again?", align = "center", font = ("Comicsans", 30, "bold"))

    play_button()
    
    turtle.tracer(True)

def turtle_reset(x=0, y=0):
    turtle.clearscreen()
    main()
    turtle_card_counter()
    
def turtle_card_counter():
    global card_counter

    turtle.tracer(False)

    background = turtle.Turtle()
    background.hideturtle()
    background.penup()
    background.pencolor("white")
    background.fillcolor("white")
    background.begin_fill()
    background.goto(-60, -15)
    background.penup()
    background.forward(120)
    background.right(90)
    background.forward(30)
    background.right(90)
    background.forward(120)
    background.right(90)
    background.forward(30)
    background.end_fill()



    counter_turtle = turtle.Turtle()
    counter_turtle.hideturtle()
    counter_turtle.penup()
    counter_turtle.goto(0, -40)
    counter_turtle.write(f"Actions: {card_counter}", align = "center", font = ("Comicsans", 15, "bold"))

    turtle.tracer(True)

def score():
    global card_counter
    global rating
    global attempt 
    global boss_count
    
    attempt = "Completed"

    turtle.tracer(False)

    score_keeper = turtle.Turtle()
    score_keeper.hideturtle()
    score_keeper.penup()
    score_keeper.goto(0, 100)

    score_keeper.write(f"Actions used: {card_counter} | Difficulty: {rating}", align = "center", font = ("Comicsans", 30, "normal"))

    if rating == 1:
        if card_counter > 4:
            attempt = "Failed"
    elif rating == 2:
        if card_counter > 5:
            attempt = "Failed"
    elif rating == 3:
        if card_counter > 7:
            attempt = "Failed"
    elif rating == 4:
        if card_counter > 9:
            attempt = "Failed"
    elif rating == 5:
        if card_counter > 13:
            attempt = "Failed"

    if attempt == "Completed":
        boss_count += 1

    score_keeper.goto(0, -150)
    score_keeper.write(f"Projects TO-DO: {boss_count}/6", align = "center", font = ("Comicsans", 30, "bold"))

    score_keeper.goto(0, 200)
    if attempt == "Completed" and boss_count == 6:
        score_keeper.write(f"Congratulations!", align = "center", font = ("Comicsans", 50, "bold"))
        score_keeper.goto(0, 150)
        score_keeper.write(f"All projects have been completed!", align = "center", font = ("Comicsans", 29, "normal"))
        score_keeper.goto(0, -200)
        score_keeper.write(f"Total Actions used: {counter_global}", align = "center", font = ("Comicsans", 30, "normal"))
        if counter_global > 50 and counter_global < 80:
            score_keeper.goto(0, -250)
            score_keeper.write(f"Overall grade: B", align = "center", font = ("Comicsans", 30, "normal"))
        if counter_global > 80:
            score_keeper.goto(0, -250)
            score_keeper.write(f"Overall grade: C", align = "center", font = ("Comicsans", 30, "normal"))
        if counter_global < 50:
            score_keeper.goto(0, -250)
            score_keeper.write(f"Overall grade: A", align = "center", font = ("Comicsans", 30, "normal"))

    elif attempt == "Completed" and boss_count < 6: 
        score_keeper.write(f"{attempt}!", align = "center", font = ("Comicsans", 50, "bold"))
        score_keeper.goto(0, 150)
        score_keeper.write(f"Would you like to continue?", align = "center", font = ("Comicsans", 29, "normal"))
    else:
        score_keeper.write(f"{attempt}. Try again.", align = "center", font = ("Comicsans", 50, "bold"))

    turtle.tracer(True)

def next_button(): #largely the same as retry except different turtles
    global attempt
    global boss_num
    general_setup()

    #go back to game
    q_next = turtle.Turtle()
    q_next.penup() 
    q_next.shape("next.gif")

    if attempt == "Completed":
        boss_num += 1

    q_next.goto(-175, 0)
    q_next.onclick(turtle_reset)

def play_button(): #todo start game loop back i think im using clearscreen() into main() onclick clear
    global boss_count
    global counter_global
    global boss_num

    boss_count = 0
    counter_global = 0
    boss_num = 1

    general_setup()

    #start game
    play = turtle.Turtle()
    play.penup()
    play.shape("play.gif")
    play.onclick(turtle_reset)

def retry_button(): #todo go back to open loop back to start menu onclick clear
    general_setup()

    #go back to game
    retry = turtle.Turtle()
    retry.penup()
    retry.shape("retry.gif")
    retry.goto(-175, 0)
    retry.onclick(turtle_reset)

def end_button(): #close program pretty much turtle on click clearscreen maybe
    #goto endscreen
    end = turtle.Turtle()
    end.penup()
    if boss_count < 6:
        end.goto(175, 0)
    else:
        end.goto(0, 0)
    end.shape("end.gif")
    end.onclick(end_screen)

def main(x=0, y=0):
    global current_health
    global card_turtle_list
    global card_counter

    boss_display()

    turtle.tracer(False)

    #creates a list of turtles everytime this function is called
    card_turtle_list = [] 
    for i in range(3):
        create_cards()

    card_placement()
    health_bar(current_health)
    
    #adds onclick to every turtle in the list
    for card in card_turtle_list:
        card.onclick(card_functionality)

    turtle.tracer(True)

    turtle_card_counter()
    difficulty_rating()

#start game
cards = read_data("cards.txt")
turtle_shapes("assets.txt")
play_screen()

turtle.mainloop()
#to use Tracy and her commands, do t.(command)
"""
Divide jobs more

directing user input more - 1. sofa, 2. dresser

makes easier check for proper input

welcome and instructions

draw objects


"""


import time
import turtle
t = turtle.Turtle()
t.speed(0) #MAKES DRAWING INSTANT
y = 1

# GETS RID OF REDUNDANT DELAYS AFTER EACH PROMPT
def read(statement):
  print(statement)
  time.sleep(2)
  print("\n")


# MAKES SCREEN BLACK (DARK)
def make_screen_black():
  t.setposition(-1500, -1500)
  t.begin_fill()
  for i in range(4):
    t.forward(3000)
    t.left(90)
  t.end_fill()

# RESETS POSITION FOR DRAWING
def reset(x, y):
  t.penup()
  t.setposition(x, y)
  t.pendown()

#DISPLAY ROOM
def room():
  t.clear()
  reset(-1000, -1000)
  t.setposition(-400, -600)
  t.setposition(400, -600)
  t.setposition(1000, -1000)
  reset(1000,1000)
  t.setposition(400, 600)
  t.setposition(-400, 600)
  t.setposition(-1000, 1000)
  reset(-400, -600)
  t.setposition(-400, 600)
  reset(400, -600)
  t.setposition(400, 600)
  reset(-150,-600)
  t.setposition(-150, 100)
  t.setposition(150, 100)
  t.setposition(150, -600)
  reset (125, -300)
  t.circle(20)

#THE ROBOT ASKS YOU WHAT YOU WANT TO DO
def action_question():
  question = input("What do you want to do now? ")
  time.sleep(2)
  x = 1 #LOOPS PROMPT BACK TO QUESTION
  while (x == 1):
    question = str.lower(question)
    if "open" in question:
      read("<Well, go on in!>") #now we need to stop this loop, can you figure it out?
      x = 2
    else:
      time.sleep(2)
      question = input("<I don't understand what you said, maybe you should say something else. Maybe you should open that door!>")


'''
#PURCHASING FROM BOB
def bob_confirmation():
    time.sleep(2)
    answer = input('"Well, do you wanna buy it?"' )
    answer = str.lower(answer)
    if "yes" in answer:
      time.sleep(2)
      read('"Let me ring that up for you!"')
    elif "no" in answer:
      time.sleep(2)
      read('"Let\'s get you something else, then, hm?"')
    else:
      time.sleep(2)
      read('"I didn\'t hear a yes- maybe you\'d like to check something else out?"')
'''
#DRAW CHAIR
def draw_chair():
  t.speed(5)
  t.clear()
  l = int(300)
  w = int(100)
  reset(0,0)
  t.begin_fill()
  t.forward(l)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.end_fill
  t.setposition(0,600)
  t.setposition(0,-300)
  t.setposition(0,0)
  t.setposition(300,0)
  t.setposition(300,-300)
  t.speed(0)

#DRAW CHAIR
def draw_table():
  l = 500
  w = 200
  t.speed(5)
  t.clear()
  reset(0,0)
  t.forward(l)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.forward(l)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.setposition(0,0)
  t.setposition(0,-200)
  t.setposition(0,-400)
  t.forward(100)
  t.setposition(100,100)
  t.forward(300)
  t.setposition(400,-400)
  t.forward(100)
  t.setposition(500,200)
  t.speed(0)

#DRAW SOFA
def draw_sofa():
  t.speed(5)
  t.clear()
  reset(0,0)
  t.setposition(200,100)
  t.setposition(200,200)
  t.setposition(0,100)
  t.setposition(0,0)
  t.setposition(-100,-50)
  t.setposition(-200,0)
  t.setposition(200,200)
  t.fillcolor("black, grey")
  t.begin_fill()
  t.setposition(400,100)
  t.setposition(400,-100)
  t.setposition(0,-300)
  t.setposition(-200,-200)
  t.setposition(-200, 0)
  t.setposition(0, -100)
  t.setposition(0,-200)
  t.setposition(400,0)
  t.setposition(200, 100)
  t.end_fill()
  t.setposition(0,0)
  t.setposition(200, -100)
  t.speed(0)

def draw_stick_figure():
  t.speed(5)
  t.clear()
  reset(0,0)
  def draw_torso():
    t.right(90)
    t.down()
    t.forward(100)
    t.up()
    t.back(100)
    t.left(90)

  def draw_legs():

      t.right(90)
      t.forward(100)
      t.right(45)
      t.down()
      t.forward(30)
      t.back(30)
      t.left(90)
      t.forward(30)
      t.back(30)
      t.right(45)
      t.up()
      t.back(100)
      t.left(90)

  def draw_arms():
      t.right(90)
      t.forward(30)
      t.left(90)
      t.down()
      t.forward(30)
      t.back(30)
      t.left(180)
      t.forward(30)
      t.back(30)
      t.left(90)
      t.up()
      t.back(30)
      t.left(90)

  def draw_head(): 
    t.down()
    t.circle(25)
    t.up()

  draw_torso()
  draw_legs()
  draw_arms()
  draw_head()
  t.speed(0)



#BOB ASKS YOU WHAT YOU WANT TO BUY
def bob_question(): 
  time.sleep(2)
  y = 1 #LOOPS PROMPT BACK TO QUESTION
  while (y == 1):
    bob_answer = input('"What would you like to buy? We have a fine selection of sofas, chairs, and tables!"')
    bob_answer = str.lower(bob_answer)
    if "sofa" in bob_answer:
      time.sleep(2)
      draw_sofa()
      bob_answer = input('"The Caleb sofa and loveseat combination from Bob\'s Discount Furniture features comfy Bob-O-Pedic Memory Foam and stylish accent pillows. With Bob\'s Discount you get both the sofa and loveseat for only $799! Pretty cool, huh?!"' )
      time.sleep(1)
      answer = input('"Well, do you wanna buy it?" (yes or no)' )
      answer = str.lower(answer)
      if "yes" in answer:
        time.sleep(2)
        read('"Let me ring that up for you!"')
        y = 2
      elif "no" in answer:
        time.sleep(2)
        read('"Let\'s get you something else, then, hm?"')
      else:
        time.sleep(2)
        read('"I didn\'t hear a yes- maybe you\'d like to check something else out?"')
    elif "chair" in bob_answer:
      time.sleep(2)
      draw_chair()
      bob_answer = input('"Rainy afternoons are far cozier when you have a cup of tea, a book and a Bob\'s living room chair, accent chair or armchair to curl up in. Bring on the storm clouds. This baby right here is $299! Pretty nice, huh?!"' )
      time.sleep(1)
      answer = input('"Well, do you wanna buy it?" (yes or no)' )
      answer = str.lower(answer)
      if "yes" in answer:
        time.sleep(2)
        read('"Let me ring that up for you!"')
        t.clear
        y = 2
      elif "no" in answer:
        time.sleep(2)
        read('"Let\'s get you something else, then, hm?"')
      else:
        time.sleep(2)
        read('"I didn\'t hear a yes- maybe you\'d like to check something else out?"')
    elif "table" in bob_answer:
      time.sleep(2)
      draw_table()
      bob_answer = input('"Add that WOW factor with a stunning dining room table. From round table tops to rectangle and square table tops, I offer plenty of options to choose from. Fancy 5 course meal not included! This one right here is $499! Pretty suave, eh?"' )
      time.sleep(2)
      answer = input('"Well, do you wanna buy it?" (yes or no)' )
      answer = str.lower(answer)
      if "yes" in answer:
        time.sleep(2)
        read('"Let me ring that up for you!"')
        t.clear
        y = 2
      elif "no" in answer:
        time.sleep(2)
        read('"Let\'s get you something else, then, hm?"')
      else:
        time.sleep(2)
        read('"I didn\'t hear a yes- maybe you\'d like to check something else out?"')
    else:
      time.sleep(2)
      read('"Get Bob\'s Discount on quality furniture for your home! Bob does the work so you can enjoy the discount on furniture, rugs, mattresses and home accents. Maybe you should ask for a "sofa", "chair", or "table"!"')
      read('"Let\'s try this again, shall we?"')

make_screen_black()
read("You wake up in a dark place, unaware of where you've been or how you got here. As you get to your feet, you hear a 'ding!' and the console behind you comes to life.")
time.sleep(3)
read("<Hello?>")
read("<Is anyone out there?>")
time.sleep(2)
input("<Can you hear me?>" )
time.sleep(2)
read("<I'm going to take that as a yes.>")
name = input("<What's your name?> ") #ACQUIRES NAME
time.sleep(2)
read("<Nice to meet you, " + name + ".>")
read("<My name is BobBot. My designation is X AE A-12.>")
read("<Please hold for parametric analysis.>")
time.sleep(2)
read("<...>")
read("<...>")
read("<...>")
read("<My analysis deduces that the power is currently off in your chambers. Let me turn it back on.>")
time.sleep(3)
room() #THE 'LIGHTS' TURN ON AND THE ROOM IS DRAWN

read("The lights flicker on.")
input("<There we go! What do you think?> ")
time.sleep(2)
read("<Duly noted. Now then, where were we?>")
action_question()
read("You enter through the doorway.")
t.clear()
read("A figure pops up in your immediate view.")
draw_stick_figure()
read('"Welcome to Bob\'s Discount Furniture!"')
read('"At Bob\'s Discount Furniture we have something that many furniture retailers don\'t have -- stores! Actual stores? Yes, over 100 coast-to-coast, surrounded by convenient parking lots. Plus these stores have doors that automatically open for you! And they have comfy, colorful and totally-affordable furniture that you can sit on before you buy!"')
time.sleep(3)
bob_question()

#BOB RINGS YOU UP
time.sleep(2)
read('You reach into your pocket to get out your wallet to find that you only have exactly the amount of money you need to pay for your furniture.')
read('Bob sees the state of your wallet and shakes his head.')
read('You hand Bob the last of your money, not even stopping to think about the wallet that just appeared out of nowhere in your pocket.')
time.sleep(3)
read('Bob rings you up and he guides you to the door.')
room()
read('Bob looks at you gently and says, "Bob\'s Discount Furniture is a retail furniture chain with locations across the multiverse. Shop online or find a nearby store at MyBobs.com!"')
time.sleep(2)
read('"I\'m sorry about this, ' + name + ' this is just the way it had to go."')
time.sleep(3)
make_screen_black()

#YOU ARE EJECTED INTO SPACE
t.fillcolor("white")
t.begin_fill()
reset(-150,-600)
t.setposition(-150, 100)
t.setposition(150, 100)
t.setposition(150, -600)
t.setposition(-150, -600)
t.end_fill()
t.fillcolor("black")

draw_stick_figure

read("The door opens into pure blackness, with white dots speckled about. You say, \"Wait... what's that?\"")
read('Not even processing that you didn\'t take your furniture with you, you turn to Bob and say,"How\'d you know my na-"')
time.sleep(3)

read("~whoosh~,you were pushed into the darkness")

make_screen_black()

read("AHHHHHHHHHH")

read("<I'm sorry, " + name + " this is the way it had to be.>")

read("As you drift out into space, you wonder exactly how you could hear the robot because sound doesn't travel in space. Eventually, you stop thinking.")


 





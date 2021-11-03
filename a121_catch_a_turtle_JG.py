# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random as rand
#-----game configuration----
score = 0
shape = "square"
color = "blue"
size = 3
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False
colors = ["red","pink","orange","purple"]
sizes = [5,4,3,2,1,0.5]
#-----initialize turtle-----
squaro = turtle.Turtle()
score_writer = turtle.Turtle()
counter = turtle.Turtle()
squaro.shape(shape)
squaro.fillcolor(color)
squaro.shapesize(size)
#-----game functions--------
def change_size():
  random_size = rand.choice(sizes)
  squaro.turtlesize(random_size)

def add_color():
  random_color = rand.choice(colors)
  squaro.color(random_color)
  squaro.stamp()
  squaro.color("blue")
def countdown():
  counter.penup()
  counter.goto(250,250)
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def update_score():
  global score
  score +=1
  score_writer.penup()
  score_writer.goto(-250,250)
  score_writer.clear()
  score_writer.write(score, font = font_setup)
  
def change_position():
  rand.randint(-200,200)
  rand.randint(-150,150)
  new_x_pos = rand.randint(-200,200)
  new_y_pos = rand.randint(-150,150)
  squaro.penup()
  squaro.goto(new_x_pos,new_y_pos)

def squaro_clicked(x,y):
  countdown()
  update_score()
  if timer > 0:
    add_color()
    change_position()
    change_size()
  else:
    squaro.hideturtle()
  
#-----events----------------
squaro.onclick(squaro_clicked)
wn = turtle.Screen()
wn.bgcolor("light green")
wn.ontimer(counter, counter_interval)
wn.mainloop()

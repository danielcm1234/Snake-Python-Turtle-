from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()
    self.alive = True
    self.pu()
    self.speed(0)
    self.color("white")
    self.shape("square")
    self.setheading(90)
    screen.onkey(self.up, "Up")
    screen.onkey(self.down, "Down")
    screen.onkey(self.left, "Left")
    screen.onkey(self.right, "Right")

    

  def up(self):
    if self.heading() != 270:
      self.setheading(90)

  def down(self):
    if self.heading() != 90:
      self.setheading(270)
      

  def left(self):
    if self.heading() != 0:
      self.setheading(180)
      

  def right(self):
    if self.heading() != 180:
      self.setheading(0)

  def move(self, body):
    self.forward(20)
    if self.xcor()>240 or self.xcor()<-240 or self.ycor()>240 or self.ycor()<-240:
      self.die(body)
    
  def die(self, body):
    self.ht()
    for i in body:
      i.ht()

class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.speed(0)
    self.pu()
    self.goto(other[-1].xcor(), other[-1].ycor())

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.speed(0)
    self.shape("circle")
    self.color("red")
    self.pu()

  def relocate(self):
    self.goto(random.randint(-220, 220), random.randint(-220, 220))

def update():
  if player.distance(apple) < 20:
    apple.relocate()
    body.append(Segment(body))
  for i in range(len(body)-1, 0, -1):
    body[i].goto(body[i-1].xcor(), body[i-1].ycor())
    player.move(body)
  for segment in body[3:]:
    if player.distance(segment) < 20:
      player.die(body)
  screen.ontimer(update, 100)

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
screen.onkeypress(update, "space")

body = []

playing_area()
apple = Apple()
apple.relocate()

player = Head(screen, body)
body.append(player)
body.append(Segment(body))

screen.exitonclick()
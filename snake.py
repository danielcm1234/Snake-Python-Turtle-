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

  def move(self):
    self.forward(1)
    if self.xcor()>240 or self.xcor()<-240 or self.ycor()>240 or self.ycor()<-240:
      self.die()
    
  def die(self):
    self.ht()


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    pass

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

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

body = []

playing_area()
apple = Apple()
apple.relocate()

player = Head(screen, body)

while True:
  player.move()
  if player.distance(apple) < 20:
    apple.relocate()



screen.exitonclick()
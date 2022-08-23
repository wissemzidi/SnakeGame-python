# import required modules
import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0



# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#3B3B3B")
# the width and height can be put as user's choice
wn.setup(width=800, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = 'red'
shapes = 'circle'
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",font=("candara", 24, "bold"))



# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 25)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 25)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 25)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 25)



wn.listen()
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

segments = []

#updating and closing screen , hack
running = True

def on_closing():
    global running
    
    running = False
    #root.destroy()
    
canvas = turtle.getcanvas()
root = canvas.winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", on_closing)

while running:
    wn.update()   #updating window

    #head dont come out the window
    if head.xcor() > 380 or head.xcor() < -380:
        head.goto(head.xcor()* -1, head.ycor())
    if head.ycor() > 280 or head.ycor() < -280 : 
        head.goto(head.xcor(), head.ycor()* -1)

    if head.distance(food) < 30:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#A7D19E")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.002
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # Checking for head collisions with body segments
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        
    time.sleep(delay)
import turtle as trtl
import random as rand


numberofWalls = 20
widthofPath = 12
wallColor = 'pink'
#Door Function(Parameters: pos) 
def drawDoor(pos):
  maze_drawer.forward(pos)
  maze_drawer.penup()
  maze_drawer.forward
  maze_drawer.forward(widthofPath*2)
  maze_drawer.pendown()
  
#Barrier Function(pos)
def drawBarriers(pos):
  maze_drawer.forward(pos)
  maze_drawer.left(90)
  maze_drawer.forward(widthofPath*2)
  maze_drawer.back(widthofPath*2)
  maze_drawer.right(90)


  

def move_runner():
  maze_runner.forward(5)
  canvas = wn.getcanvas()
  xy = maze_runner.position()

def goUp():
  maze_runner.setheading(90)
  maze_runner.forward(5)
def goDown():
  maze_runner.setheading(270)
  maze_runner.forward(5)
def goRight():
  maze_runner.setheading(0)
  maze_runner.forward(5)
def goLeft():
  maze_runner.setheading(180)
  maze_runner.forward(5)


#Config 
maze_drawer = trtl.Turtle()
maze_drawer.pensize(5)
maze_drawer.pencolor(wallColor)
maze_drawer.speed('fastest')

maze_runner = trtl.Turtle(shape="circle")
maze_runner.fillcolor("blue")
maze_runner.turtlesize(0.7)
print(maze_runner.turtlesize()) 
maze_runner.penup()
maze_runner.goto(-widthofPath*2, widthofPath*2)
maze_runner.pendown()



  


wallLength = widthofPath
for i in range(numberofWalls):
  wallLength += widthofPath

  if (i > 5):
    maze_drawer.left(90)
    # randomize location of doors and barriers in wall
    door = rand.randint(widthofPath*2, (wallLength - widthofPath*2))
    barrier = rand.randint(widthofPath*2, (wallLength - widthofPath*2))

    while abs(door - barrier) < widthofPath: 
      door = rand.randint(widthofPath*2, (wallLength - widthofPath*2)) 

    if (door < barrier):
      drawDoor(door)
      drawBarriers(barrier - door - widthofPath*2)
      # draw the rest of the wall
      maze_drawer.forward(wallLength - barrier)
    else: 
      drawBarriers(barrier)
      drawDoor(door - barrier)
      # draw the rest of the wall
      maze_drawer.forward(wallLength - door - widthofPath*2)
      
maze_drawer.hideturtle()

#Event Listeners
wn = trtl.Screen()
wn.onkeypress(goUp, 'Up')
wn.onkeypress(goDown, 'Down')
wn.onkeypress(goLeft, 'Left')
wn.onkeypress(goRight, 'Right')
wn.onkeypress(move_runner, 'g')
wn.listen()
wn.mainloop()




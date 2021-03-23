import turtle as trtl
import random as rand


numberofWalls = 20
widthofPath = 12
wallColor = 'red'
#Door Function(Parameters: pos - Position of Door and Barrier) 
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


#Config 
maze_drawer = trtl.Turtle()
maze_drawer.pensize(5)
maze_drawer.pencolor(wallColor)
maze_drawer.speed('fastest')




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

wn = trtl.Screen()

wn.listen()
wn.mainloop()




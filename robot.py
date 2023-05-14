#!/usr/bin/python3.5
# -*- coding: latin-1 -*-

#Global Stuff
#from os import system
import sys
# Import graphic gaming stuff
import pygame
# Importing math Library
import math

#DEBUG 1=on 0=off
debug=0

#The circle
circlecenterx=-3
circlecentery=4
circumference=(10 * math.pi)
radius=circumference / (2 * math.pi)

#The grid
gridstartx=0
gridstarty=0
gridwidth=20
xmargin=gridwidth
ymargin=gridwidth
gridminx=circlecenterx - int(radius) - 1
gridmaxx=circlecenterx + int(radius) + 2
gridminy=circlecentery - int(radius) - 1
gridmaxy=circlecentery + int(radius) + 2
gridresminx=xmargin
gridresmaxx=(gridmaxx - gridminx - 1) * gridwidth + xmargin
gridresminy=ymargin
gridresmaxy=(gridmaxy - gridminy - 1)  * gridwidth + ymargin
gridresx=0
gridresy=0

#The robot
robotx=circlecenterx
roboty=circlecentery

#The screen resolution
screenmax_x=800
screenmax_y=600

#Text configuration
font_size = 18

#PyGames initialization values
pygame.init()
size = (screenmax_x,screenmax_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RobotCirle")
font = pygame.font.Font(None, font_size)


#Key bindings
pturn_left = pygame.K_a
pturn_right = pygame.K_d
pgo_forward = pygame.K_w
pgo_backward = pygame.K_s
pquit = pygame.K_q
pbreak = pygame.K_b

#Colors
light_grey = (64,64,64)
black = (0,0,0)
yellow = (255,255,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
grey = (127,127,127)
red = (255,0,0)
royalblue = (65,105,225)

#DEBUG
if debug:
	print ( "screenmax_x" , screenmax_x )
	print ( "screenmax_y" , screenmax_y )
	print ( "circlecenterx" , circlecenterx )
	print ( "circlecentery" , circlecentery )
	print ( "circumference" , circumference )
	print ( "radius" , radius )
	# This will print the value of pi in the output
	print ( "PI" , math.pi)

def main():
	drawgrid()
	drawcircle()
	drawrobot()	
	pygame.display.flip()
	getinput()

def getinput():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if (event.key == pquit) or (event.key == pbreak):
        	#print ( "quit" )
          quit()
        elif (event.key == pturn_left) or (event.key == pygame.K_LEFT):
          moverobot("W")
        elif (event.key == pgo_forward) or (event.key == pygame.K_UP):
          moverobot("N")
        elif (event.key == pturn_right) or (event.key == pygame.K_RIGHT):
          moverobot("E")
        elif (event.key == pgo_backward) or (event.key == pygame.K_DOWN):
          moverobot("S")
        #  return "b"
        #  break

def drawgrid():
	for x in range (gridminx,gridmaxx):
		getresxy(x,0)
		pygame.draw.line(screen,royalblue,[gridresx,gridresminy],[gridresx,gridresmaxy],2)
		text = font.render(str(x), 1, white)
		screen.blit(text, (gridresx - gridwidth/4, 0))
		#print ("minx", gridminx, "maxx", gridmaxx, "x", x, "minresx", gridresminx, "maxresx", gridresmaxx, "gridresx", gridresx, "miny", gridminy, "maxy", gridmaxy, "y", "y", "minresy", gridresminy, "maxresy", gridresmaxy, "gridresy" , "gridresy")
	for y in range (gridminy,gridmaxy):
		getresxy(0,y)
		pygame.draw.line(screen,royalblue,[gridresminx,gridresy],[gridresmaxx,gridresy],2)
		text = font.render(str(y), 1, white)
		screen.blit(text, (0, gridresy - gridwidth/4))
		#print ("minx", gridminx, "maxx", gridmaxx, "x", x, "minresx", gridresminx, "maxresx", gridresmaxx, "gridresx", gridresx, "miny", gridminy, "maxy", gridmaxy, "y", y, "minresy", gridresminy, "maxresy", gridresmaxy, "gridresy" , gridresy)

def getresxy(x,y):
	global gridresx
	global gridresy
	gridresx=(x - gridminx + 1)*gridwidth
	gridresy=(y - gridminy + 1)*gridwidth		
	#print ("getresxy", x, y, gridresx, gridresy)

def drawcircle():
	for degrees in range (0,360):
		rads=math.radians(degrees)
		circlex=math.cos(rads) * radius + circlecenterx
		circley=math.sin(rads) * radius + circlecentery
		getresxy(circlex,circley)
		#print("degrees", degrees, circlex, circley, gridresx, gridresy)
		pygame.draw.rect(screen,yellow,[gridresx-1,gridresy-1,2,2],1)
		#pygame.display.flip()

def drawrobot():
	getresxy(robotx,roboty)
	#print("degrees", degrees, circlex, circley, gridresx, gridresy)
	pygame.draw.rect(screen,red,[gridresx-2,gridresy-2,6,6])
	#print("robotxy",robotx,roboty)
	#pygame.display.flip()

def moverobot(move):
	global robotx
	global roboty
	tempx=robotx
	tempy=roboty
	if (move == "N") or (move == "n"):
		tempy=tempy-1
	elif (move == "S") or (move == "s"):
		tempy=tempy+1
	elif (move == "E") or (move == "e"):
	  tempx=tempx+1
	elif (move == "W") or (move == "w"):
	  tempx=tempx-1
	if checkrobot(tempx,tempy):
		#print ("check")
		robotx=tempx
		roboty=tempy
		drawrobot()
		pygame.display.flip()

def checkrobot(x,y):
	x=x - circlecenterx
	y=y - circlecentery
	#print ("xy", x, y, "z", math.sqrt(x ** 2 + y ** 2), radius)
	if math.sqrt(x ** 2 + y ** 2) <= radius:
		return 1
	else:
		return 0

def quit():
  pygame.quit()
  sys.exit()

main()  
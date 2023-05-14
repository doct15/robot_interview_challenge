# robot_interview_challenge

So I was at a bbq with a bunch of other tech friends and the discussion turned to programming job interview questions.

The question was could you move a robot in a circle, given only the circumference, and tell when the robot left the circle.

This repro solves that problem.

This uses python 3 with pygame (for graphics)

Wet the circle initial x,y center coordinates and the circle circumference.

		#The circle
		circlecenterx=-3
		circlecentery=4
		circumference=(10 * math.pi)
		radius=circumference / (2 * math.pi)

Do not change the radius formula

The robot starts at the center of the circle

> #The robot
> robotx=circlecenterx
> roboty=circlecentery

Once you start the app, you can go the pygame screen and move the robot around with the arrow keys.
q = quit


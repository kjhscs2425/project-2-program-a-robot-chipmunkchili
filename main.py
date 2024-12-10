# Import the robot control commands from the library
from simulator import robot
import time

ninety_deg_turn_time = 1.525

def move_forward(seconds):
    robot.motors(1, 1, seconds)
def move_backward(seconds):
    robot.motors(-1, -1, seconds)
def turn_right(seconds):
    robot.motors(-1, 1, seconds)
def turn_left(seconds):
    robot.motors(1, -1, seconds)
    
def draw_circle(num_times, go_forward):
    for i in range(num_times):
        if go_forward:
            turn_left(0.2)
            move_forward(0.1)
        else:
            turn_right(0.2)
            move_backward(0.1)

def draw_rectangle(width, height):
    turn_right(ninety_deg_turn_time)
    move_forward(height / 2)
    turn_left(ninety_deg_turn_time)
    move_forward(width / 2)
    turn_left(ninety_deg_turn_time)
    move_forward(height)
    turn_left(ninety_deg_turn_time)
    move_forward(width)
    turn_left(ninety_deg_turn_time)
    move_forward(height)
    turn_left(ninety_deg_turn_time)
    move_forward(width/2)

shape = input("Would you like me to go in a circle or a rectangle? ")

if shape == "circle":
    draw_circle(38, True)
    draw_circle(38, False)
elif shape == "rectangle":
    draw_rectangle(5, 1)

def too_close_to_move_forward(left_dist, right_dist):
    return left_dist <= 100 or right_dist <= 100

def too_close_to_move_backward(left_dist, right_dist):
    return left_dist >= 375 or right_dist >= 375

first_move = input("Would you like me to move forward or backward? ")
seconds = int(input("How long would you like me to do this? "))
if first_move == "forward":
    while seconds > 0.1:
        robot.motors(1,1,0.1)            
        left_dist, right_dist = robot.sonars()
        seconds -= 0.1
        too_close = too_close_to_move_forward(left_dist, right_dist)
        if too_close:
            robot.motors(-1, 1, ninety_deg_turn_time * 2)
            seconds -= ninety_deg_turn_time * 2
elif first_move == "backward":
    while seconds > 0.1:
        robot.motors(-1,-1,0.1)            
        left_dist, right_dist = robot.sonars()
        seconds -= 0.1
        too_close = too_close_to_move_backward(left_dist, right_dist)
        if too_close:
            robot.motors(-1, 1, ninety_deg_turn_time * 2)
            seconds -= ninety_deg_turn_time * 2

def move_2():
    spin_direction = input("Which direction would you like me to spin first? Right or left? ")
    if spin_direction == "right":
        seconds = int(input("How long would you like me to do this? "))
        turn_right(seconds)
        turn_left(seconds)
    elif spin_direction == "left":
        seconds = int(input("How long would you like me to do this? "))
        turn_left(seconds)
        turn_right(seconds)
    else:
        move_2()

move_2()

print("Now I will tell you how far I am from each wall!")
for i in range(4):
    turn_right(ninety_deg_turn_time)
    left_dist, right_dist = robot.sonars()
    average_dist = (left_dist*right_dist)/2
    print(f"Average distance to wall {i + 1} is {average_dist}")

def fun():
    had_fun = input("Did you have fun (yes or no)? ")
    if had_fun == "yes":
        print("Yay! So did I!")
        robot.exit()
    else:
        fun()

fun()
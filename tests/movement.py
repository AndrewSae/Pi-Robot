from gpiozero import Robot, DistanceSensor 
from time import sleep


robot = Robot(left=(16,12), right=(21,20))


while True:
    print("moving forward")
    robot.forward()
    sleep(2)
    print("moving right")
    robot.right()
    sleep(2)
    print("moving left")
    robot.left()
    sleep(2)
    print("moving backward")
    robot.backward()
    sleep(2)
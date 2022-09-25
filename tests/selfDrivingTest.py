import math
from gpiozero import Robot, DistanceSensor 
from time import sleep
import random

robot = Robot(left=(16,12), right=(21,20))

front_sensor = DistanceSensor(echo=23, trigger=24)
back_sensor = DistanceSensor(echo=25, trigger=8)
front_right_sensor = DistanceSensor(echo=22, trigger=27)
front_left_sensor = DistanceSensor(echo=17, trigger=4)

right_sensor = DistanceSensor(echo=5, trigger=6)
left_sensor = DistanceSensor(echo=11, trigger=9)

run = True

while run:

    sleep(0.1)
    if front_sensor.distance * 100 <= 20:
        #stop the robot
        robot.stop()
        # get the readings from the front left and right sensors
        front_read = front_sensor.distance * 100
        left_read = left_sensor.distance * 100
        right_read = right_sensor.distance * 100

        # print out all of the readings 
        print("stoped somthing blocking front")
        print("Front: " + str(front_read))
        print("left: " + str(left_read))
        print("right: " + str(right_read))


        if left_read <= right_read and right_read >= 20:
            print("right")
            while front_sensor.distance * 100 <= 20:
                robot.right()
                sleep(.1)
            robot.stop()
            print("done" + str(front_sensor.distance * 100))

        elif right_read <= left_read and left_read >= 20:
            print("left")
            while front_sensor.distance * 100 <= 20:
                robot.left()
                sleep(.1)
            robot.stop()
            print("done" + str(front_sensor.distance * 100))


    elif front_right_sensor.distance * 100 <= 20:
        robot.left()
        sleep(2)
        robot.stop()

    elif front_left_sensor.distance * 100 <= 20:
        robot.right()
        sleep(2)
        robot.stop()


    else:
        robot.forward(speed=.5)
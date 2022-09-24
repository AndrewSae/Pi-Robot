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
        robot.stop()

        front_read = front_sensor.distance * 100

        left_read = left_sensor.distance * 100
        right_read = right_sensor.distance * 100

        
        print("stoped somthing blocking front")
        print("Front: " + str(front_read))
        print("left: " + str(left_read))
        print("right: " + str(right_read))



        if left_read <= right_read and left_read >= 20:
            robot.left()
            sleep(3)
            robot.stop()
            if front_sensor.distance * 100 <=20:
                  print("stuck")


        elif right_read >= left_read and right_read >= 20:
            robot.right()
            sleep(3)
            robot.stop()
            if front_sensor.distance * 100 <=20:
                print("stuck")


      

    elif front_right_sensor.distance * 100 <= 20:
        robot.stop()

        front_read = front_sensor.distance * 100
        front_right_read = front_right_sensor.distance * 100
        front_left_read = front_left_sensor.distance * 100
        

        print("stoped somthing blocking right side")
        print("Right: " + str(front_right_read))


        if front_left_read and front_read >= 20:
            robot.left()
            sleep(2)
            robot.stop()
        else:
            while front_left_read and front_read <= 20:
                robot.backward()
            robot.stop()
            robot.left()
            sleep(2)
            robot.stop()


    elif front_left_sensor.distance * 100 <= 20:
        robot.stop()

        front_read = front_sensor.distance * 100
        front_right_read = front_right_sensor.distance * 100
        front_left_read = front_left_sensor.distance * 100
        

        print("stoped somthing blocking left side")
        print("Left: " + str(front_left_read))

        

        if front_right_read and front_read >= 20:
            robot.left()
            sleep(2)
            robot.stop()
        else:
            while front_right_read and front_read <= 20:
                robot.backward()
            robot.stop()
            robot.right()
            sleep(2)
            robot.stop()


    else:
        robot.forward()
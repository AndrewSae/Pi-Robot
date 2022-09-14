from gpiozero import DistanceSensor

front_sensor = DistanceSensor(echo=23, trigger=24)
back_sensor = DistanceSensor(echo=25, trigger=8)
front_right_sensor = DistanceSensor(echo=22, trigger=27)
front_left_sensor = DistanceSensor(echo=17, trigger=4)

right_sensor = DistanceSensor(echo=5, trigger=6)
left_sensor = DistanceSensor(echo=11, trigger=9)


print("front" + str(front_sensor.distance * 100))
print("front right" + str(front_right_sensor.distance * 100))
print("front_left" + str(front_left_sensor.distance * 100))

print("right" + str(right_sensor.distance * 100))
print("left" + str(left_sensor.distance * 100))
print("back" + str(back_sensor.distance * 100))
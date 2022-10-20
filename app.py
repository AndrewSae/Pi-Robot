from flask import Flask,render_template,Response, request, redirect, url_for
from gpiozero import Robot, DistanceSensor
from time import sleep
from threading import Thread

robot = Robot(left=(16,12), right=(21,20))

front_sensor = DistanceSensor(echo=23, trigger=24)
back_sensor = DistanceSensor(echo=25, trigger=8)
front_right_sensor = DistanceSensor(echo=22, trigger=27)
front_left_sensor = DistanceSensor(echo=17, trigger=4)

right_sensor = DistanceSensor(echo=5, trigger=6)
left_sensor = DistanceSensor(echo=11, trigger=9)

app=Flask(__name__)



global runScript

def selfDriving():
    global runScript
    sleep(.1)
    while runScript:
        if front_sensor.distance * 100 <= 20:

            robot.stop()

            front_read = front_sensor.distance * 100
            left_read = left_sensor.distance * 100
            right_read = right_sensor.distance * 100

            if left_read <= right_read and right_read >= 20:
                while front_sensor.distance * 100 <= 20:
                    robot.right() 
                    sleep(.1)
                robot.stop()

            elif right_read <= left_read and left_read >= 20: 
                while front_sensor.distance * 100 <= 20:
                    robot.left()
                    sleep(.1)
                robot.stop()

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
    print("done")
            

@app.route('/', methods=["GET","POST"])
def index():
    global runScript
    runScript = False

    robot.stop()

    if request.method == 'POST':
        if request.form.get('Forward') == 'Forward':
            robot.forward()

        elif  request.form.get('Left') == 'Left':
            robot.left()

        elif  request.form.get('Right') == 'Right':
            robot.right()

        elif  request.form.get('Backward') == 'Backward':  
            robot.backward()

        elif  request.form.get('Stop') == 'Stop':  
            robot.stop()

    return render_template('index.html')

@app.route('/page2', methods=["GET","POST"])

def page2():

    robot.stop()
    global runScript

    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            runScript = True
            
            t1 = Thread(target=selfDriving)

            t1.start()

        if request.form.get('Stop') == 'Stop':
            runScript = False
            print("stoped")
                

    return render_template('page2.html')


if __name__=="__main__":
    app.run(host="0.0.0.0") 

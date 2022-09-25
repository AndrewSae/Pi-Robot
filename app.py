from distutils.core import run_setup
from flask import Flask,render_template,Response, request, redirect, url_for
from gpiozero import Robot, DistanceSensor
from time import sleep
import cv2 
from threading import Thread


# setup the motor conrtoller with GPIOZERO (ROBOT)
robot = Robot(left=(16,12), right=(21,20))


front_sensor = DistanceSensor(echo=23, trigger=24)
back_sensor = DistanceSensor(echo=25, trigger=8)
front_right_sensor = DistanceSensor(echo=22, trigger=27)
front_left_sensor = DistanceSensor(echo=17, trigger=4)

right_sensor = DistanceSensor(echo=5, trigger=6)
left_sensor = DistanceSensor(echo=11, trigger=9)

app=Flask(__name__)

camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        # read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
global runScript
runScript = False

def thread():
    if request.form.get('Stop') == 'Stop':
         print("stoping script")
         global runScript
         runScript = False
         robot.stop()
def thread2():
    global runScript

    while runScript:

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


@app.route('/', methods=["GET","POST"])
def index():
    print(request.method)
    robot.stop()

    global speed
    if request.method == 'POST':
        if request.form.get('Forward') == 'Forward':
            print("moving forward")
            robot.forward(speed=.5)

        elif  request.form.get('Left') == 'Left':
            print("moving left")
            robot.left(speed=.5)
   
        elif  request.form.get('Right') == 'Right':
            print("moving Right")
            robot.right(speed=.5)
   
        elif  request.form.get('Backward') == 'Backward':  
            print  ("moving backward")
            robot.backward(speed=.5)

        elif  request.form.get('Stop') == 'Stop':  
            print("stoping")
            robot.stop()

    

        else:
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")  

    return render_template('index.html')

@app.route('/page2', methods=["GET","POST"])
def page2():
    global runScript
    runScript = False
    robot.stop()
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            print("starting script")
            runScript = True
            t1 = Thread(target=thread)
            t2 = Thread(target=thread2)
            t1.start()
            t2.start()
            t1.join()
            t2.join()

    return render_template('page2.html')


@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(host="0.0.0.0") 
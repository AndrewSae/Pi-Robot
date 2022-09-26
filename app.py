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
            
            while runScript:
                sleep(.1)
                print("running")
                if request.form.get('Stop') == 'Stop':
                    print("stoping script")
                    runScript = False
                    break 
                





    return render_template('page2.html')


@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(host="0.0.0.0") 
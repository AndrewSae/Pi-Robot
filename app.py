from flask import Flask,render_template,Response, request
from gpiozero import Robot, DistanceSensor
from time import sleep
import cv2 

# setup the motor conrtoller with GPIOZERO (ROBOT)
robot = Robot(left=(20,21), right=(12,16))

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


@app.route('/', methods=["GET","POST"])
def index():
    print(request.method)
    global speed
    if request.method == 'POST':
        if request.form.get('Forward') == 'Forward':
            print("moving forward")
            robot.forward()

        elif  request.form.get('Left') == 'Left':
            print("moving left")
            robot.left()
   
        elif  request.form.get('Right') == 'Right':
            print("moving Right")
            robot.right()
   
        elif  request.form.get('Backward') == 'Backward':
            print("moving backward")
            robot.backward()

    

        else:
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")  

    return render_template('index.html')



@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(host="0.0.0.0") 
# Pi Robot 🤖
### A Raspberry Pi Zero W powered robot

## About This Project
  - Made With Python with a web server powered by Flask
  - The actual pages on the web server were made with HTML5, CSS3, and Bootstrap
  - The web server has controls for the robot and is also used to start/stop the self-driving script
  - The self-driving script allows the robot to use the six ultrasonic sensors to drive around without hitting anything
  - This robot moves via the 4 TT motors powered by a motor controller
 
 ## Parts List
 
| Part |      Quantity      |
|----------|:-------------:|
| Raspberry Pi Zero W | x1 |
| GPIO Terminal Block |    x1   | 
| LewanSoul 4WD Robot Kit |    x1   | 
| Metal Gear Motor TT |    x4   | 
| L298N Motor Controller |    x1   | 
| Ultrasonic Sensors hc-sr04 |    x6   | 
| Mounts For Ultrasonic Sensors |    x4   | 
| USB portable charger |    x1   | 
|6x1 AA Battery Box |    x1   | 
|Male To Female Jumper Wires |    N/A   | 

(the Ultrasonic Sensor mounts can be found in the parts directory)




 
 ## Problems I had
  - I wanted to add a camera to the robot to view through the web server, but the Pi Zero was not powerful enough to handle the camera, causing the video to be laggy. To Combat this issue I replaced the Pi Zero with a Pi 4B, which solved my problem for a little bit. The thing Is that the Pi 4B died on me so I had to put the Pi Zero back in and remove the camera future.
  - The ultrasonic sensors are cheap so when you order them some did not work when they were delivered. Also because they are cheap sometimes when on the robot they would just stop working entirely making the program crash causing me to frequently replace them. 
 
## Photos



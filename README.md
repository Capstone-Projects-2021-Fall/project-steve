![STEVE_Cropped_Logo](https://user-images.githubusercontent.com/56208195/141854169-afe79893-a3eb-4e2d-a4e4-c11ea588ea07.png)

## System Overview

Self-driving Totally Electronic Vehicular Escort, or STEVE for short, is a fully autonomous RC car that can navigate to a predetermined location in any large indoor complex. Whether the indoor complex is a large office, a school, a shopping mall, a hospital, or an airport, STEVE will navigate the user, avoiding any obstacles along the way, and lead them to their destination courteously. The user will have the option to either use a mobile application to tap buttons to control STEVE or an Amazon Alexa enabled device (which consists of nearly any device with an internet connection & a microphone) to communicate with STEVE using their voice. STEVE will then use an onboard speaker to communicate any necessary messages with the user. An alternative option to make STEVE more accessible for users who have disabilities would be to grab a tether that is attached to the car.

The car will use an onboard Raspberry Pi to communicate with a remote Python server, sending information about STEVE’s current state including speed, turning value, and what his camera sees. The Remote Server will use certain libraries such as TensorFlow and OpenCV that will then process the information and decide STEVE’s next movements. The server will also send the general directions to the location to STEVE, if it knows how to get there. In addition to the Raspberry Pi and the receiver card, onboard the car will also be a camera (to take visual input) and a speaker (to convey messages to users). In terms of storing routes, a Firebase Realtime Database will be used for long term storage. Finally, the mobile application will be built using Ionic (a web framework for building mobile apps), as well as an Amazon Alexa skill for users to be able to interact with STEVE using their voice and tell him where to go.

Usually, whenever someone goes to a new building for the first time, they do so with some sort of purpose in mind. Whether they are arriving at an office building for a business meeting or an airport in a foreign country to fly back home, they have a destination within the building in mind. If they are lucky, this destination will have a standard room number that tells them which floor it is on, but even then, it is hard to know where on the floor it is. Then you must also account for the many times where there are not standard room numbers, and someone needs to find “Mr. Doe’s Office” or “Room Garfield”. All in all, it is generally very difficult to know exactly where you are supposed to go whenever you enter a new building. 

This is where STEVE comes in. It eliminates that anxiety someone gets when they walk in a building for the first time and have no idea where they are going. It eliminates that fear of being late to a business meeting or missing a flight due to getting lost. STEVE guides people so they can worry about other things. 

![image](https://user-images.githubusercontent.com/56208195/141853765-397b55b2-7cfd-4757-a3aa-ad9c363dab8a.png)

## Hardware Requirements

- [Exceed Racing Desert Short Course Truck RC Car](https://www.amazon.com/gp/product/9269802094/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
- [Raspberry Pi 3 Model B+ ](https://www.amazon.com/gp/product/B07P4LSDYV/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
- [Raspberry Pi Camera ](https://www.amazon.com/Raspberry-Camera-Module-Megapixels-Sensor/dp/B07L82XBNM/ref=sr_1_3?keywords=raspberry+pi+3+camera&qid=1636512675&sr=8-3)
- [Servo Controller Card](https://www.amazon.com/HiLetgo-PCA9685-Channel-12-Bit-Arduino/dp/B01D1D0CX2/ref=asc_df_B01D1D0CX2/?tag=hyprod-20&linkCode=df0&hvadid=312106042452&hvpos=&hvnetw=g&hvrand=4270474016124585645&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9007311&hvtargid=pla-439629573722&psc=1&tag=&ref=&adgrpid=62821668875&hvpone=&hvptwo=&hvadid=312106042452&hvpos=&hvnetw=g&hvrand=4270474016124585645&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9007311&hvtargid=pla-439629573722)
- [Speaker(s)](https://www.amazon.com/gp/product/B075M7FHM1/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
- Any USB Power Bank
- Mobile Phone(s)

## Installation

The following guide is regarding how to set up the software and going forward it is assumed a STEVE car is already assembled. For instructions on assembling the hardware, see [Donkey Car's guide](https://docs.donkeycar.com/guide/build_hardware/) on the topic.

1. Download the Remote Server files on your computer of choice (this computer will effectively become the Remote Server)
2. Follow along with [this guide](https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/) provided by Donkey Car up to and including step 10 to install Raspbian along with the required dependencies 
3. SSH into the Raspberry Pi from your computer (instructions on how to do this in the aforementioned guide)
4. Clone this repo into the Raspberry Pi through the command line
```
git clone https://github.com/Capstone-Projects-2021-Fall/project-steve.git
```
4. use the command line to navigate into the RPi folder
```
cd project-steve/RPi
```
5. Start the RPi server
```
python3 server.py
```
6. Back on the Remote Server (the computer used in step 1), launch the Remote Server's server file
7. Install the mobile app on your phone of choice
8. Now the Remote Server & RPi are running! All you have to do is train your routes & click them on the Mobile App to watch STEVE play them back!

## Training a Route

Note: The Remote Server must be running to train a route

1. SSH onto the RPi
2. Navigate to the RPi folder
```
cd project-steve/RPi
```
3. Connect an Xbox Controller to the RPi. This can be done via bluetooth or USB. If there is no prior knowledge of using bluetooth on a Raspberry Pi it is recommended to use USB. If USB is not an option, [here is a guide](https://www.cnet.com/tech/computing/how-to-setup-bluetooth-on-a-raspberry-pi-3/) to connect via bluetooth
4. Run the RPi client
```
python3 client.py
```
5. The RPi is now reading inputs from the controller, use the right trigger to make STEVE accelerate & use the left analog stick to make STEVE turn
6. Drive STEVE to the desired destination
7. Upon finishing the route, press the 'start' button on the Xbox Controller
8. Back on the RPi terminal, type the name of the route that was just executed and press enter
9. The route will now be uploaded to the Remote Server & Firebase. Once the program has finished executing, you may place STEVE back at his starting point and click on the route in the mobile app to watch him play it back!

## Contributors

Blake Patterson <br>
Garrett Bowser <br>
Hunter Nuss <br>
Marcel Millan <br>
Tarekegne Aboye <br>

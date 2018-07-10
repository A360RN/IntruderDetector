# Intruder Detector Project

## Instructions for Arduino

### Requirements:

* Having an Arduino (Project was made with UNO) as well as an HC-SR501 sensor.

### Installation:

* Download or clone the source code.

* Compile the .ino file that is inside arduino folder and run the program in your Arduino.

## Instructions for Raspberry Pi 3

### Requirements:

* Having a Raspberry Pi 3 with Python 3 installed, as well as a webcam.

### Installation:

* Connect the webcam to your Raspberry Pi 3.

* Download or clone the source code.

* Set the needed environment variables for authenticating with Firebase, Twitter and Twilio.

* Go inside raspberry folder.

* Execute the following commands to install the python libraries required (requirements.txt method with pip coming soon !): `pip install pyserial twython twilio pyrebase`

* Run `python client.py`




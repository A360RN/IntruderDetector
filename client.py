import serial
import subprocess
import datetime
import os
import time
import pyrebase
from twython import Twython
from twilio.rest import Client

flag = False

twitter_consumer_key = os.environ['TWITTER_CONSUMER_KEY']
twitter_consumer_key_secret = os.environ['TWITTER_CONSUMER_KEY_SECRET']
twitter_access_token = os.environ['TWITTER_ACCESS_TOKEN']
twitter_access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
twitter = Twython(
    twitter_consumer_key,
    twitter_consumer_key_secret,
    twitter_access_token,
    twitter_access_token_secret
)
    
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilioClient = Client(twilio_account_sid, twilio_auth_token)

ser = serial.Serial("/dev/ttyACM0", baudrate=9600)

firebaseConfig = {
  "apiKey": "AIzaSyBvDnIBvcyBvjlk9yN02IxhpY84dauJDdM",
  "authDomain": "sistemasdistribuidosg4.firebaseapp.com",
  "databaseURL": "https://sistemasdistribuidosg4.firebaseio.com",
  "storageBucket": "sistemasdistribuidosg4.appspot.com"
};

firebase = pyrebase.initialize_app(firebaseConfig)

def sistema_handler(message):
    if message['path'] == '/flag':
        global flag
        flag = message['data']
        if (flag):
            ser.write(b'A')
        else:
            ser.write(b'B')
    
db = firebase.database()
sistema_stream = db.child("sistema").stream(sistema_handler)

def updateTwitterStatus():
    now = datetime.datetime.now().isoformat()
    subprocess.check_call(['./webcam.sh', now])
    imageName = now + '.jpg'
    photo = open(imageName, 'rb')
    response = twitter.upload_media(media=photo)
    message = 'Intruso detectado, fecha: ' + now
    twitter.update_status(status=message, media_ids=[response['media_id']])

def sendSms(message):
    twilioClient.messages.create(
        body=message,
        from_='(859) 594-7466',
        to='+51943182392'
    )

while True:
    read_ser=ser.read()
    if(read_ser==b'1' and flag):
        intentos = 0
        db.child("intruso").update({"flag": True})
        #sendSms('#ZuñeChipi')
        while intentos < 5:
            updateTwitterStatus()
            intentos+=1
            time.sleep(5)
        
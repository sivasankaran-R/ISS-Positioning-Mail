import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "agarwaltest3@gmail.com"
PASSWORD = "qwerty123()"

MY_LAT = 10.972460
MY_LNG = 79.770264


def is_iss_near():
  #iss- position
  response = requests.ge("http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()

  longitude  = float(data["iss_position"]["longitude"])
  latitude = float(data["iss_position"]["latitude"])

  #check iss position is near to mu position
  if MY_LAT-5 <= latitude <=MY_LAT+5 and MY_LNG-5 <= longitude <=MY_LNG+5:
    return True

def is_night():
  #sunrise and sunset time of our position
  parameter = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
  }
  response = requests.get("https://api.sunrise-sunset.org/json",params = parameter)
  response.raise_for_status()
  data = response.json()
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

  now_time = datetime.now().hour
  #checking for the night time
  if now_time >= sunset or now_time <= sunrise:
    return True

while True:
  time.sleep(60)
  if is_iss_near and is_night:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls
    connection.login(user=MY_EMAIL,password=PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs=MY_EMAIL,
      msg="Subject:ISS overhead\n\n Getout see the sky !"
      )






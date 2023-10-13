#


import requests
import smtplib
from datetime import datetime
import time


My_lat="YOUR LATITUDE ON THE MAP "
My_lng="YOUR lONGITUDE  ON THE MAP "

response=requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data=response.json()

iss_latitude=float(data["iss_position"]["latitude"])
iss_longitude=float(data["iss_position"]["longitude"])



parameters={

  "lat":My_lat,
  "lng":My_lng,
  "formatted":0,

  
}


response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)

response.raise_for_status()

data=response.json()

sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])

sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])# first devide for me the data into two parts depending on the t , then a list of two items will be formatted , then format for me the second item depending on the colmn, then print for me the first item whuch is the hour .



time_now=datetime.now()

my_time=int(time_now.hour)

while True :
  time.sleep(60)#wait 60 seconds every time before executing the below code!
  if ((My_lat-3) <= (iss_latitude) >= My_lat) and  ((My_lng-3) <= (iss_longitude) >= My_lng) and sunrise<my_time>sunset :
    #SINCE THE ISS IS VERY FAST , SO WE HAVE TO GIVE A BUFFER LATTITUDE AND LONGITUDE IN ORDER TO CATCH IT , 
    #AND WE WILL GET IT ONLY IN THE SUNSET TO HAVE A CLEAR VISSION !V
  
    my_email="YOUR EMAIL" 
    passwordd=" YOUR EMAIL PASSWORD "
  
    with smtplib.SMTP("smtp.gmail.com") as connection :
      
        connection.starttls()
        connection.login(user=my_email,password=passwordd)
        connection.sendmail(from_addr=my_email,to_addrs="TO ANOTHER EMAIL",msg="subject:ISS Location\n\n Hey look , the ISS is just above you !" )
        connection.close()
     
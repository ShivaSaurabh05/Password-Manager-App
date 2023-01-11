import smtplib
import time
from checker import *
from datetime import datetime

current_time = datetime.now().hour

my_email = "shivasaurabh0506@gmail.com"
my_password = "9835277421Sh?"
reciever_mail = "shivasaurabh05@gmail.com"

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = reciever_mail,
            msg="Subject: Time to look up ✨🎈\n\nThe ISS is above you."
        )
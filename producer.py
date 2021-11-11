from kafka import KafkaProducer
import time
import json 
from datetime import datetime
import random

from numpy.random.mtrand import rand   

producer = KafkaProducer(bootstrap_servers='20.120.14.159:9092') 

dirr = ["N", "NW", "W", "SW", "S", "SE", "E", "NE"]


while(True):
    dic = {
        "hum" : random.randrange(1,100),
        "tem" : round(random.uniform(0.00, 99.99), 2),
        "vin" : random.choice(dirr)
    }
    payload = json.dumps(dic).encode('utf-8')
    producer.send('17055',payload)
    time.sleep(15)
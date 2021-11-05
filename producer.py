from kafka import KafkaProducer
from time import sleep 
import json 
from datetime import datetime  

producer = KafkaProducer(bootstrap_servers='20.120.14.159:9092') 

producer.send('17055',b'Este es un mensaje')
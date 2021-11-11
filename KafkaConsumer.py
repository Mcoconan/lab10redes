from kafka import KafkaConsumer
from kafka import TopicPartition
import kafka
from kafka.client_async import KafkaClient
import json
import matplotlib.pyplot as plt

tem = []
hum = []
vin = []
count = 0
def forgiving_json_deserializer(v):
    
    try:
        return json.loads(v.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        log.exception('Unable to decode: %s', v)
        return None

consumer = KafkaConsumer('17055',bootstrap_servers='20.120.14.159:9092', value_deserializer = forgiving_json_deserializer )
for i in consumer:
     count = count + 1
     print (consumer)
     payload = i.value
     tem.append(float(payload['tem']))
     hum.append(int(payload['hum']))
     vin.append(payload['vin'])
     if count % 15 == 0:
          fig = plt.figure()
          plt.plot(hum)
          plt.title("Grafica de humedad")
          plt.xlabel ("tiempo")
          plt.ylabel ("Humedad")
          fig2 = plt.figure()
          plt.plot (tem)
          plt.title("Grafica de temperatura")
          plt.xlabel("Tiempo")
          plt.ylabel("Temperatura")
          plt.show()

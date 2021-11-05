from kafka import KafkaConsumer
from kafka import TopicPartition
import kafka
from kafka.client_async import KafkaClient

consumer = KafkaConsumer('17055',bootstrap_servers='20.120.14.159:9092')
for msg in consumer:
     print (msg)



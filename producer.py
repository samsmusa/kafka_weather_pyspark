import json
from datetime import datetime
from random import choice
from time import sleep

from kafka import KafkaProducer

kafka_server = ["192.168.0.166"]

topic = "test_topic"

producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

random_values = [1, 2, 3, 4, 5, 6, 7]

while True:
    random_value = choice(random_values)
    data = {
        "test_data": {
            "random_value": random_value
        },
        "timestamp": str(datetime.now()),
        "value_status": "High" if random_value > 5 else "Low"
    }
    print(data)
    producer.send(topic, data)
    producer.flush()
    sleep(3)
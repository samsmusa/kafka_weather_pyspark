import json
from datetime import datetime
from time import sleep
from random import choice
from kafka import KafkaProducer

location = "London"
key = "6566557e0232479c86e45625230903"

url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no"

kafka_bootstrap_servers = ["192.168.0.166"]
kafka_topic_name = "weather_topic"


producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

json_message = None
city_name = None

temperature = None
wind_mph = None
pressure_mb = None
humidity =  None

def get_weather_data(url:str):
    api_response = 
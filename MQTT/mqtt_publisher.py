# mqtt_publisher.py
import paho.mqtt.client as mqtt
import time

BROKER_ADDRESS = "localhost"
TOPIC = "topic/learning"
MESSAGE = "There is rain going on!"

# 1. Create a new MQTT client instance
client = mqtt.Client()

# 2. Connect to the broker
client.connect(BROKER_ADDRESS, 1883, 60)

# 3. Publish the message # publish(topic, payload, qos, retain) # qos=0: at most once, qos=1: at least once, qos=2: exactly once
client.publish(TOPIC, MESSAGE)
print(f"Published message '{MESSAGE}' to topic '{TOPIC}'")

# 4. Disconnect from the broker
client.disconnect()
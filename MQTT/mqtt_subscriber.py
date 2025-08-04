# mqtt_subscriber.py
import paho.mqtt.client as mqtt


BROKER_ADDRESS = "localhost"
TOPIC = "topic/learning"

# This function is called when the client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(TOPIC)
    else:
        print(f"Failed to connect, return code {rc}\n")

# This function is called whenever a message is received on a subscribed topic
def on_message(client, userdata, msg):
    print(f"Received message on topic '{msg.topic}': {msg.payload.decode()}")

# 1. Creating a new MQTT client instance
client = mqtt.Client()

# 2. Assigning the callback functions
client.on_connect = on_connect
client.on_message = on_message

# 3. Connecting to the broker
client.connect(BROKER_ADDRESS, port=1883, keepalive=60)

# 4. Starting a background thread to handle network traffic and dispatch callbacks
print(f"Subscribing to topic '{TOPIC}'...")
client.loop_forever() # loop_forever() is a blocking call that processes messages and reconnections automatically.

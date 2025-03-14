import paho.mqtt.client as mqtt

# MQTT broker details
broker = "157.173.101.159"
port = 1883
topic = "/student_group/light_control"

# Define message handler
def on_message(client, userdata, message):
    msg = message.payload.decode()
    if msg == "ON":
        print("💡 Light is TURNED ON")
    elif msg == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print(f"❌ Unknown message received: {msg}")

# Setup MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to broker
client.connect(broker, port, 60)

# Subscribe to topic
client.subscribe(topic)

print(f"🚀 Listening for MQTT messages on {topic}...")

# Keep listening
client.loop_forever()

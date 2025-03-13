import paho.mqtt.client as mqtt

# Local MQTT broker configuration
broker = "localhost"
port = 1883
topic = "/student_group/light_control"

# Define message handler
def on_message(client, userdata, message):
    msg = message.payload.decode()
    if msg == "ON":
        print("💡 Light is TURNED ON")
    elif msg == "OFF":
        print("💡 Light is TURNED OFF")

# Setup MQTT client
client = mqtt.Client()
client.connect(broker, port, 60)

# Subscribe to the topic
client.subscribe(topic)
client.on_message = on_message

print("🚀 Listening for MQTT messages...")
client.loop_forever()

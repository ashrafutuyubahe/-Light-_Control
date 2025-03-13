import paho.mqtt.client as mqtt

# Broker configuration
broker = "157.173.101.159"
port = 1883
topic = "/student_group/light_control"

# Callback when connected to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}")

# Callback when a message is received
def on_message(client, userdata, message):
    msg = message.payload.decode()
    if msg == "ON":
        print("💡 Light is TURNED ON")
    elif msg == "OFF":
        print("💡 Light is TURNED OFF")

# Create MQTT client
client = mqtt.Client()

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker and start the loop
client.connect(broker, port, 60)
client.loop_forever()

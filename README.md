🏮 MQTT Light Control
This project of mine is a simple MQTT-based Light Control system that allows you to control a virtual light bulb through a web interface using MQTT messages.

🚀 Features

✅ Connects to an MQTT broker using WebSockets
✅ Sends "ON" and "OFF" commands to control the light
✅ Updates the light status dynamically based on MQTT messages
✅ Simulates the light bulb turning on and off in the frontend

🛠️ How It Works

Connects to an MQTT broker at ws://157.173.101.159:9001/mqtt.
Publishes "ON" or "OFF" messages to the topic /student_group/light_control.
Listens for messages on the same topic and updates the UI accordingly.
Simulates the light bulb status visually using CSS and JavaScript.

📦 Required Packages (Dependencies)
before run plz install this Dependencies
 -> if using npm :  npm install mqtt  
 -> using CDN in Html : <script src="https://unpkg.com/mqtt/dist/mqtt.min.js"></script>


🌐 How to Run
1. install required pa
Open the index.html file in your browser.
run  this command to run the script(light_simulation.py)  -> python light_simulation.py
Click "Turn ON" or "Turn OFF" in the browser page(index.html) to send MQTT messages.
Observe the light bulb simulation changing based on the received status.

📂 Project Structure

here is the structure of project

├── index.html
├── light_simulation.py
└── README.md


🧪 Technologies Used
HTML, CSS, JavaScript
MQTT.js (WebSocket connection)


import requests
import random
import time

while True:
    sensor_data = {
        "temperature": random.uniform(70, 95),
        "pressure": random.uniform(5.0, 6.5),
        "vibration": random.uniform(0.01, 0.12),
        "speed": random.uniform(1350, 1550)
    }

    response = requests.post("http://localhost:5000/predict", json=sensor_data)
    print("Sensor data:", sensor_data, "| Prediction:", response.json())
    time.sleep(3)

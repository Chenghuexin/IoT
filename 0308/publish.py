import paho.mqtt.client as mqtt
import time
client = mqtt.Client(callback_api_version = mqtt.CallbackAPIVersion.VERSION1)
client.connect("test.mosquitto.org", 1883, 60)

while True:
    msg = "[{\"macAddr\":\"0000000020200002\",\"data\":\"ac05\",\"id\":\"01\",\"extra\":{\"port\":2,\"txpara\":\"2\"}}]"
    client.publish("GIOT-GW/DL/000080029c0ff65e", msg)
    time.sleep(5)
#訂閱broker但並未將資料過濾
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("GIOT-GW/UL/80029C1E38D2")

def on_message(client, userdata, msg):
    
    msgStr = str(msg.payload)
    data = json.loads(msgStr[2:-1])
    # data = json.load(msgStr)
    # msgIndex = msgStr.index("macAddr")
    # print(msgStr[2:-1])
    print(data[0]['macAddr'])
    

client = mqtt.Client(callback_api_version = mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect  #設定連線動作
client.on_message = on_message  #設定接收訊息動作
client.connect("test.mosquitto.org", 1883, 60) #connect(host, port=1883, keepalive=60, bind_address="")

try:
    while True:
        client.loop()
except KeyboardInterrupt:
    print("\nclose")
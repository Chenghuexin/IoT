import paho.mqtt.client as mqtt
import time

#訂閱broker但並未將資料過濾
import paho.mqtt.client as mqtt
import json
import random
def publish(data):
    # connect
    client = mqtt.Client(callback_api_version = mqtt.CallbackAPIVersion.VERSION1)
    client.connect("test.mosquitto.org", 1883, 60)

    # id should change everytime after publishing
    # let range of id in [1~9]
    id = random.randint(1, 100)
    msg = "[{\"macAddr\":\"0000000020200002\",\"data\":\"" + data + "\",\"id\":\"" + str(id) + "\",\"extra\":{\"port\":2,\"txpara\":\"2\"}}]"
    client.publish("GIOT-GW/DL/000080029c0ff65e", msg)
    time.sleep(5)
    # id = 0
    # while True:
    #     id += 1
    #     id %= 10
    #     msg = "[{\"macAddr\":\"0000000020200002\",\"data\":\"" + data + "\",\"id\":\"0" + str(id) + "\",\"extra\":{\"port\":2,\"txpara\":\"2\"}}]"
    #     client.publish("GIOT-GW/DL/000080029c0ff65e", msg)
    #     time.sleep(5)
    # print('publish')
    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("GIOT-GW/UL/80029C1E38D2")

def on_message(client, userdata, msg):
    
    msgStr = str(msg.payload) # change message to string
    data = json.loads(msgStr[2:-1]) # choose the string we want and convert it to  json

    if(data[0]['macAddr']=="0000000020200002"): # filter other macAddr
        hex_ascii = data[0]['data'] # get data

        byte_data = bytes.fromhex(hex_ascii) # convert hexadecimal ASCII to bytes

        int_ascii = float(byte_data.decode()) # convert bytes to integer ASCII

        # print(str(int_ascii))
        print('ok')

        # judge
        if(int_ascii > 25.5):
            publish('31')
        else:
            publish('30')
    
    
    

client = mqtt.Client(callback_api_version = mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect  #設定連線動作
client.on_message = on_message  #設定接收訊息動作
client.connect("test.mosquitto.org", 1883, 60) #connect(host, port=1883, keepalive=60, bind_address="")

try:
    while True:
        client.loop()
except KeyboardInterrupt:
    print("\nclose")

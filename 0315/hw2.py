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

    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("GIOT-GW/UL/80029C1E38D2")

def on_message(client, userdata, msg):
    
    msgStr = str(msg.payload) # change message to string
    data = json.loads(msgStr[2:-1]) # choose the string we want and convert it to  json

    if(data[0]['macAddr']=="0000000020200002"): # filter other macAddr
        hex_ascii_temperature = data[0]['temperature'] # get temperature data
        hex_ascii_humidity = data[0]['humidity'] #get humidity data

        byte_data_temperature = bytes.fromhex(hex_ascii_temperature) # convert hexadecimal ASCII temperature to bytes
        byte_data_humidity = bytes.fromhex(hex_ascii_humidity) # convert hexadecimal ASCII humidity to bytes


        int_ascii_temperature = float(byte_data_temperature.decode()) # convert bytes to integer ASCII temperature
        int_ascii_humidity = float(byte_data_humidity.decode()) # convert bytes to integer ASCII humidity
        

        # print(str(int_ascii))
        print('ok')

        # judge
        if(int_ascii_temperature > 30.5 or int_ascii_humidity > 75.5):
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



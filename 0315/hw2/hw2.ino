#include <Arduino_HS300x.h>
#include <avr/dtostrf.h>
#include <string.h>

int uplink_count = 0, downlink_count = 0;

float old_temp = 0;
float old_hum = 0;

String data;
void setup() {
  Serial.begin(9600);        //設定硬體串列埠速率
  Serial1.begin(115200);      //設定軟體串列埠速率
  delay(1000);
  Serial.println("sip reset");
  Serial1.write("sip reset");    //初始化
  while(!Serial1.available()>0){} 
  Serial.println(Serial1.readString());
  delay(1000);
  
  Serial.println("mac join abp");   //設定join mode
  Serial1.write("mac join abp");
  while(!Serial1.available()>0){} 
  Serial.println(Serial1.readString());
  delay(1000);

  Serial.println("sip set_log info");   //關閉debug模式
  Serial1.write("sip set_log info");
  while(!Serial1.available()>0){} 
  Serial.println(Serial1.readString());
  delay(500);

  Serial.println("mac save");   //儲存設定
  Serial1.write("mac save");
  while(!Serial1.available()>0){} 
  Serial.println(Serial1.readString());
  delay(500);     
  Serial.println("==============");

  if (!HS300x.begin()) {
    Serial.println("Failed to initialize humidity temperature sensor!");
    while (1);
  }
}

void loop() {
  String data;
  if(uplink_count < 100){
    Serial.println("start measure");
    // read all the sensor values
    float temperature = HS300x.readTemperature();
    float humidity    = HS300x.readHumidity();
    String divider = "2B"; //+
    String temperature_hex;
    String humidity_hex;

    if (abs(old_temp - temperature) >= 0.5 || abs(old_hum - humidity) >= 1 )
    {
      // print each of the sensor values
      Serial.print("Temperature = ");
      Serial.print(temperature);
      Serial.println(" °C");

      Serial.print("Humidity    = ");
      Serial.print(humidity);
      Serial.println(" %");

      // print an empty line
      Serial.println();

      // wait 1 second to print again
      delay(1000);
    }
    
    // convert the data type of temperature and humidity to hex
    // float(origin) -> char array -> string

    temperature_hex = String(temperature);
    humidity_hex = String(humidity);

    // float(origin) -> char array
    //After converting to hex, number of character will be doubled 
    char reply_temp[temperature_hex.length()*2 + 1]; 
    char reply_hum[humidity_hex.length()*2 + 1];
    temperature_hex.toCharArray(reply_temp, temperature_hex.length() * 2 + 1);
    humidity_hex.toCharArray(reply_hum, humidity_hex.length() * 2 + 1);

    // char -> string
    String uplink_temp = "";
    String uplink_hum = "";
    for(int i = 0;i < strlen(reply_temp); i++){
      uplink_temp += String(reply_temp[i], HEX);
    }

    for(int i = 0;i < strlen(reply_hum); i++){
      uplink_hum += String(reply_hum[i], HEX);
    }

    String instruction = "mac tx ucnf 2 " + uplink_temp + divider + uplink_hum;

  
    Serial.println(instruction);   
    Serial1.write((const uint8_t*)instruction.c_str(), instruction.length());

    uplink_count += 1;

    while(!Serial1.available()>0){}
    data=Serial1.readString();
    // Serial.println(data);
    
    int pos=data.indexOf("mac rx 2");
    if(pos>0)
    {
      int pos1=data.indexOf(">> Ok");
      if(pos1==-1)
      {
        String info=data.substring(pos+9,data.length());
        Serial.print("xxx(");
        Serial.print(info);
        Serial.println(")");
      }
      else
      {
        String info=data.substring(pos+9,pos1-4);
        Serial.print("yyy(");
        Serial.print(info);
        Serial.println(")");      
      }
    }
    delay(5000);
  }
  

  
    
  
}


/*
  int pos=data.indexOf("mac rx 2");
  if(pos>0)
  {
    int pos1=data.indexOf(">> Ok");
    if(pos1==-1)
    {
      String info=data.substring(pos+9,data.length());
      Serial.print("xxx(");
      Serial.print(info);
      Serial.println(")");
    }
    else
    {
      String info=data.substring(pos+9,pos1-4);
      Serial.print("yyy(");
      Serial.print(info);
      Serial.println(")");      
    }
  }
  delay(5000);
}
*/
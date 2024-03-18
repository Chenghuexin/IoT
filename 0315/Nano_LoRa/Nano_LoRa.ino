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
}

void loop() {
  String data;
  Serial.println("mac tx ucnf 2 1237");   
  Serial1.write("mac tx ucnf 2 1237");
  while(!Serial1.available()>0){}
  data=Serial1.readString();
  Serial.println(data);
  delay(5000);
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
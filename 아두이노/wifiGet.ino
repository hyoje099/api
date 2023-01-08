#include<ESP8266WiFi.h>
#include<ESP8266HTTPClient.h>

char*wifi_name="UCA-2.4G";
char*password="052708001";

void serup(){
    Serial.begin(115200);
    Wifi.begin(wifi_name,password);
    while (wifi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.print("Connecting...");
    }
    
}
void loop(){
    if(wifi.status() == WL_CONNECTED){
        HTTPClient http;
        String getReuqestURL = "http://127.0.0.1:8000/";
        String name ="wonjun";
        String age = "50";

        getRequestURL +="/name/";
        getRequestURL +=name;
        getRequestURL +="/age/";
        getRequestURL += age;

        http.behin(getRequestURL);

        int httpCode = http. GET();
        if(httpCode>0){
            String payload =http.getString();
            Serial.println(payload);
        }
        http.end();
    }
    delay(3000);
}
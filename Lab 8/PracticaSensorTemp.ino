#include <DHT.h>
#define TIPO_SENSOR DHT11 
#define SENSOR_PIN 6 

DHT sensor(SENSOR_PIN, TIPO_SENSOR);

void setup(){
  Serial.begin(9600);
  sensor.begin();
}

void loop(){
  delay(1000);

  float humed = sensor.readHumidity();
  float temper = sensor.readTemperature();

  Serial.print("Humedad: ");
  Serial.print(humed);
  Serial.print("%     ");
  Serial.print("Temperatura: ");
  Serial.print(temper);
  Serial.print("°C");
  Serial.print("\n");
}

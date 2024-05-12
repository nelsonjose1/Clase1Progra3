int rele = 2;

void setup() {
  pinMode(rele, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  Serial.println("Rele Encendido");
  digitalWrite(rele, HIGH);
  delay(2000);
  Serial.println("Rele Apagado");
  digitalWrite(rele, LOW);
  delay(2000);
}
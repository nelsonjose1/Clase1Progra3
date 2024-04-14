const int ledPin13 = 13;
const int ledPin12 = 12;
const int ledPin10 = 10;
const int buttonPin1 = 4;
const int buttonPin2 = 6;
const int buttonPin3 = 8; 

bool leerPotenciometro = true;

void setup() {
  pinMode(ledPin13, OUTPUT);
  pinMode(ledPin12, OUTPUT);
  pinMode(ledPin10, OUTPUT);
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
  pinMode(buttonPin3, INPUT_PULLUP);  
  Serial.begin(9600);
}

void loop() {
  if (leerPotenciometro) {
    int pot = analogRead(A0);
    Serial.println(pot);
    delay(10);
  }
  int buttonState1 = digitalRead(buttonPin1);
  int buttonState2 = digitalRead(buttonPin2);
  int buttonState3 = digitalRead(buttonPin3);
  
  if (buttonState1 == LOW) {
    Serial.println("Inorden ejecutado");
    digitalWrite(ledPin13, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin13, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin12, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin10, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin12, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin12, LOW);
    Serial.println(0);
    delay(1000);
    Serial.println("Inorden terminado");
  }
  if(buttonState2 == LOW){
    Serial.println("Posorden ejecutado");
    digitalWrite(ledPin10, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin10, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin13, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin13, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin12, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin12, LOW);
    Serial.println(0);
    delay(1000);
    Serial.println("Posorden terminado");
  }
  if(buttonState3 == LOW){
    Serial.println("Preorden ejecutado");
    digitalWrite(ledPin12, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin12, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin10, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin10, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin13, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin13, LOW);
    Serial.println(0);
    Serial.println("Preorden terminado");
  }

}

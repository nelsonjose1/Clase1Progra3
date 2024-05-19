#include <Stepper.h>
#include <Servo.h>

int pasos = 2048;
Stepper motor(pasos, 8, 10, 9, 11);
Servo servoMotor;  

void setup() {
  servoMotor.attach(2);  
  motor.setSpeed(10);
  Serial.begin(9600);  
}

void loop() {
  if (Serial.available() > 0) {
    char numMonitorSerial = Serial.read();

    if (numMonitorSerial == '1') {
      MotorStepper();
    } else if (numMonitorSerial == '2') {
      MotorServo();
    }
  }
}

void MotorStepper() {
  Serial.println("Inicio Motor Stepper");
  motor.step(pasos);
  delay(500);
  motor.step(-pasos);
  delay(500);
  Serial.println("Fin Motor Stepper");
}

void MotorServo() {
  Serial.println("Inicio Motor Servo");

  servoMotor.write(0);  
  delay(500);

  servoMotor.write(90);  
  delay(500);

  servoMotor.write(180); 
  delay(500);

  servoMotor.write(90);  
  delay(500);

  servoMotor.write(0);  
  delay(500);

  Serial.println("Fin Motor Servo");
}

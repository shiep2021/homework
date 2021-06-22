#include <Servo.h>
long item;
Servo servo_7;
Servo servo_6;

void setup()
{
  item = 0;
  Serial.begin(9600);
  servo_6.attach(6);
  servo_7.attach(7);
}

void loop()
{
  if (Serial.available() > 0) {
    item = String(Serial.readStringUntil('a')).toInt();
    switch (item) {
     case 1:
      servo_7.write(0);
      servo_6.write(0);
      delay(500);
      break;
     case 2:
      servo_7.write(45);
      servo_6.write(45);
      delay(500);
      break;
     case 3:
      servo_7.write(90);
      servo_6.write(90);
      delay(500);
      break;
     default:
      servo_7.write(135);
      servo_6.write(135);
      delay(500);
      break;
    }

  }

}

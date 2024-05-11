#include <Servo.h>

#define MAGNET_CATCH 13
#define SERVO_FACTOR 0.5

Servo topArmServo;
Servo midArmServo;
Servo btmArmServo;
Servo baseArmServo;

int prevPositionTopArm = 0;
int prevPositionMidArm = 170;
int prevPositionBtmArm = 0;
int prevPositionBaseArm = 10;

void setup() {
  topArmServo.attach(5);
  midArmServo.attach(6);
  btmArmServo.attach(3);
  baseArmServo.attach(7);

  pinMode(MAGNET_CATCH, OUTPUT);
  digitalWrite(MAGNET_CATCH, LOW);

  Serial.begin(9600);
  Serial.println("Homing device");
  home();

  Serial.println("EOS");
}

void loop() {

  Serial.println("Ready for Input");

  while (Serial.available() < 1) {
    delay(100);
  }

  // Get user data
  String data = Serial.readStringUntil('\n');
  String command = data.substring(0, data.indexOf(','));
  command.toLowerCase();

  int position = data.substring(data.indexOf(',') + 1).toInt();

  if (command.indexOf("mid") != -1) {

    // Check for limits
    if ((position >= 20) && (position <= 170)) {

      // Move Arm to position
      moveArm(midArmServo, position, prevPositionMidArm);
      Serial.println("Mid Arm reached position ");
      prevPositionMidArm = position;
    }

    else {
      Serial.println("Limits of Mid arm is [20, 170]");
    }
  }

  else if (command.indexOf("top") != -1) {

    // Check for limits
    if ((position <= 150) && (position >= 0)) {

      // Move to position
      moveArm(topArmServo, position, prevPositionTopArm);

      Serial.println("Top Arm reached position ");
      prevPositionTopArm = position;

    } else {
      Serial.println("Position Limits of top arm is: [0, 150]");
    }
  }

  else if (command.indexOf("btm") != -1) {

    if ((position <= 100) && (position >= 0)) {

      // Move to position
      moveArm(btmArmServo, position, prevPositionBtmArm);

      Serial.println("Bottom Arm reached position ");
      prevPositionBtmArm = position;

    } else {
      Serial.println("Position Limits of top arm is: [0, 90]");
    }
  }

  else if (command.indexOf("bas") != -1) {

    // Check for limits
    if ((position <= 110) && (position >= 10)) {

      // Move to position
      moveArm(baseArmServo, position, prevPositionBaseArm);

      Serial.println("Base Arm reached position ");
      prevPositionBaseArm = position;

    } else {
      Serial.println("Position Limits of base arm is: [90, 180]");
    }
  }

  else if (command.indexOf("home") != -1) {
    home();
  }

  else if (command.indexOf("drop") != -1) {
    // Get the arm to the top to avoid collision
    home();

    // Move the base arm first & Btm arm last to ensure that the arm does not get stuck below the cardboard surface
    moveArm(baseArmServo, 120, prevPositionBaseArm);
    prevPositionBaseArm = 120;

    // moveArm(midArmServo, 100, prevPositionMidArm);
    moveArm(topArmServo, 0, prevPositionTopArm);
    prevPositionTopArm = 0;

    moveArm(btmArmServo, 90, prevPositionBtmArm);
    prevPositionBtmArm = 90;

    // Turn off magnet
    digitalWrite(MAGNET_CATCH, LOW);
  }

  else if (command.indexOf("pick") != -1) {
    digitalWrite(MAGNET_CATCH, HIGH);
  }

  else if (command.indexOf("rest") != -1) {
    home();

    moveArm(baseArmServo, 45, prevPositionBaseArm);
    prevPositionBaseArm = 45;

    moveArm(topArmServo, 0, prevPositionTopArm);
    prevPositionTopArm = 0;

    moveArm(midArmServo, 130, prevPositionMidArm);
    prevPositionMidArm = 130;

    moveArm(btmArmServo, 90, prevPositionBtmArm);
    prevPositionBtmArm = 90;
  }

  else if (command.indexOf("mag") != -1) {
    if (digitalRead(MAGNET_CATCH)) {
      Serial.println("Magnet ON");
    } else {
      Serial.println("Magnet OFF");
    }
  }

  else if (command.indexOf("help") != -1) {
    printHelp();
  }

  Serial.print("link to ");
  Serial.println(position);

  printTable();
}


void moveArm(Servo s, int position, int prevPosition) {
  for (float pos = prevPosition; pos != position; pos += (prevPosition > position ? -1 : 1)) {
    s.write(pos);
    delay(15);
  }
}

String formatInteger(int value) {
  String formatted = String(value);
  while (formatted.length() < 3) {
    formatted = " " + formatted;
  }
  return formatted;
}

void home() {
  btmArmServo.write(0);
  prevPositionBtmArm = 0;

  // Need some time - to avoid collision after drop
  delay(100);

  midArmServo.write(170);
  prevPositionMidArm = 170;

  topArmServo.write(0);
  prevPositionTopArm = 0;

  baseArmServo.write(10);
  prevPositionBaseArm = 10;
}

void printTable() {
  Serial.println();

  Serial.println("      | Top | Mid | Btm | Bas |");
  Serial.println("|-----|-----|-----|-----|-----|");
  Serial.println("| Min |   0 |  20 |   0 |  10 |");

  Serial.print("| Cur | ");
  Serial.print(formatInteger(prevPositionTopArm));
  Serial.print(" | ");
  Serial.print(formatInteger(prevPositionMidArm));
  Serial.print(" | ");
  Serial.print(formatInteger(prevPositionBtmArm));
  Serial.print(" | ");
  Serial.print(formatInteger(prevPositionBaseArm));
  Serial.println(" |");

  Serial.println("| Max | 150 | 170 | 100 | 110 |");

  Serial.println();
}

void printHelp() {
  Serial.println("-----------------------------------------------------------------------------------------------");
  Serial.println("Command: <arm>, <position>");
  Serial.println("Desc: Move arm to position");
  Serial.println("<arm> can take values top, mid, btm, bas");
  Serial.println("<position> is an angle & should be in the range of [Max, Min] found in the joint axis table");

  Serial.println();
  Serial.println("Command: help");
  Serial.println("Desc: Print this help menu");

  Serial.println();
  Serial.println("Command: pick");
  Serial.println("Desc: Turn on the electromagnet");

  Serial.println();
  Serial.println("Command: home");
  Serial.println("Desc: Move to pre-determined home position : (0, 170, 0, 10)");

  Serial.println();
  Serial.println("Command: drop");
  Serial.println("Desc: Drop the picked up item at pre-detemined drop position : (0, *, 90, 120)");

  Serial.println();
  Serial.println("Command: rest");
  Serial.println("Desc: Move the robot to mechanical rest position : (0, 130, 90, 45)");

  Serial.println();
  Serial.println("Command: table");
  Serial.println("Desc: Print the joint axis table");

  Serial.println();
  Serial.println("Command: mag");
  Serial.println("Desc: Print the magnet status (on / off)");

  Serial.println();
  Serial.println("Joint Axis notation: (top, mid, btm, bas)");
  Serial.println("-----------------------------------------------------------------------------------------------");

}
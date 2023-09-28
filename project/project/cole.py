import os
import time

class TrafficManagementSystem:
    def welcome(self):
        os.system("clear")
        tt = time.time()
        ti = time.localtime(tt)
        print("\n\n\n\n\n\n\n\n\n\n", asctime(ti))
        self.delay_1()
        os.system("clear")
        print("' '")
        print("' HEARTY WELCOME TO '")
        print("' '")
        print("' TRAFFIC MANAGEMENT SYSTEM '")
        print("' '")
        print("' '")
        print("' '")
        print("' '")
        print("' ENTER YOUR DESIRED OPTION: '")
        print("' '")
        print("' Press 1 to record new vehicles '")
        print("' Press 2 to get record of challan '")
        print("' Press 3 to search record of vehicles '")
        print("' Press 4 to search traffic control booths '")

# First of all, we define the pins where we have connected the LEDs.
red_1 = 13
yellow_1 = 12
green_1 = 11
red_2 = 10
yellow_2 = 9
green_2 = 8
red_3 = 7
yellow_3 = 6
green_3 = 5
red_4 = 4
yellow_4 = 3
green_4 = 2

def direction_1_green():
    # green LED of direction 1 will turn ON
    digitalWrite(red_1, LOW)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, HIGH)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_2_yellow():
    # yellow LED of direction 2 will turn ON
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, LOW)
    digitalWrite(yellow_2, HIGH)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_2_green():
    # green LED of direction 2 will turn ON
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, LOW)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, HIGH)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_3_yellow():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, LOW)
    digitalWrite(yellow_3, HIGH)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_3_green():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, LOW)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, HIGH)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_4_yellow():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, LOW)
    digitalWrite(yellow_4, HIGH)
    digitalWrite(green_4, LOW)

def direction_4_green():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, LOW)
    digitalWrite(yellow_4, HIGH)
    digitalWrite(green_4, LOW)
    import time

red_1 = 2
yellow_1 = 3
green_1 = 4
red_2 = 5
yellow_2 = 6
green_2 = 7
red_3 = 8
yellow_3 = 9
green_3 = 10
red_4 = 11
yellow_4 = 12
green_4 = 13

def direction_1_green():
    digitalWrite(red_1, LOW)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, HIGH)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_2_yellow():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, LOW)
    digitalWrite(yellow_2, HIGH)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_2_green():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, LOW)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, HIGH)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_3_yellow():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, LOW)
    digitalWrite(yellow_3, HIGH)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_3_green():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, LOW)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, HIGH)
    digitalWrite(red_4, HIGH)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, LOW)

def direction_4_yellow():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, LOW)
    digitalWrite(yellow_4, HIGH)
    digitalWrite(green_4, LOW)

def direction_4_green():
    digitalWrite(red_1, HIGH)
    digitalWrite(yellow_1, LOW)
    digitalWrite(green_1, LOW)
    digitalWrite(red_2, HIGH)
    digitalWrite(yellow_2, LOW)
    digitalWrite(green_2, LOW)
    digitalWrite(red_3, HIGH)
    digitalWrite(yellow_3, LOW)
    digitalWrite(green_3, LOW)
    digitalWrite(red_4, LOW)
    digitalWrite(yellow_4, LOW)
    digitalWrite(green_4, HIGH)

def setup():
    # Declaring all the LED's as output
    for i in range(2, 14):
        pinMode(i, OUTPUT)

def loop():
    # In the loop function, we controlled the signal one by one to control the flow of traffic.
    direction_1_green()
    time.sleep(5)
    direction_2_yellow()
    time.sleep(3)
    direction_2_green()
    time.sleep(5)
    direction_3_yellow()
    time.sleep(3)
    direction_3_green()
    time.sleep(5)
    direction_4_yellow()
    time.sleep(3)
    direction_4_green()
    time.sleep(5)
    direction_1_yellow()
    time.sleep(3)
 
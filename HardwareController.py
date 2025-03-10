import RPi.GPIO as GPIO
import Freenove_DHT as DHT
from Status import Status
import time

class HardwareController:

    MAXIMUM_SAFE_TEMP = 21

    def __init__(self, test_mode=False):
        self.is_test_mode = test_mode
        GPIO.setmode(GPIO.BCM)

        self.current_temp = 0

        # self.led = 1
        self.buzzer = 17
        self.servo = 27
        self.dht = 4
        
        self.tones = [440, 1440]
        self.angles = [3, 12]

        # GPIO.setup(self.led, GPIO.OUT)
        GPIO.setup(self.buzzer, GPIO.OUT)
        GPIO.setup(self.servo, GPIO.OUT)
    
        
        self.alarm = GPIO.PWM(self.buzzer, 440)
        self.door = GPIO.PWM(self.servo, 50)
        
        self.door.start(0)
        
        self.status = Status.NONE
        
    def read_temp(self):
        self.temp_sensor = DHT.DHT(self.dht) 
        if self.temp_sensor.readDHT11() == 0:   
            self.current_temp = self.temp_sensor.getTemperature()
            
        return self.current_temp

    def check_temperature(self, ui_callback_function):
        current_temp = self.read_temp()

        if not self.is_test_mode:
            if current_temp > self.MAXIMUM_SAFE_TEMP and self.status != Status.ALERT:
                print('Alert temp')
                self.status = Status.ALERT
                ui_callback_function("ALERT")
                self.alarm.start(50)
                self.door.start(self.angles[0])
                time.sleep(0.25)
                self.door.stop()
                # turn LED ON              
            elif current_temp <= self.MAXIMUM_SAFE_TEMP and self.status != Status.SAFE:
                print('Safe temp')
                self.status = Status.SAFE
                self.alarm.stop()
                self.door.start(self.angles[1])
                time.sleep(0.25)
                self.door.stop()
                # turn LED OFF


    def activate_test_mode(self):
        self.is_test_mode = True

    def deactivate_test_mode(self):
        self.is_test_mode = False

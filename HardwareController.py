# import RPi.GPIO as GPIO

class HardwareController:

    MAXIMUM_SAFE_TEMP = 21

    def __init__(self, test_mode=False):
        self.is_test_mode = test_mode
        # GPIO.setmode(GPIO.BCM)

        # self.led = 1
        # self.alarm = 2
        # self.servo = 3
        # self.temp_sensor = 4

        # GPIO.setup(self.led, GPIO.OUT)
        # GPIO.setup(self.alarm, GPIO.OUT)
        # GPIO.setup(self.servo, GPIO.OUT)
        # GPIO.setup(self.temp_sensor, GPIO.IN)

    def read_temp(self):
        return 20 # Read from GPIO

    def check_temperature(self, ui_callback_function):
        current_temp = self.read_temp()

        if not self.is_test_mode:
            if current_temp > self.MAXIMUM_SAFE_TEMP:
                ui_callback_function("ALERT")
                # sound alarm
                # door action
                # turn LED ON
            else:
                print('Safe temp')
                #  alarm
                # door action
                # turn LED OFF


    def activate_test_mode(self):
        self.is_test_mode = True

    def deactivate_test_mode(self):
        self.is_test_mode = False
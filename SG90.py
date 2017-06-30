import RPi.GPIO as GPIO
from tkinter import *

# servo TowerPro SG90 or SG92R
freq = 50.0
deg_min = 0.0
deg_max = 180.0
dc_min = 5.0
dc_max = 10.0

# motor driver GVS output 12, 18, 22, 31
servo = 31

def init():
    global p
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servo, GPIO.OUT)
    p = GPIO.PWM(servo, freq)
    p.start(0)

def convert_dc(degree):
    dc = ((float(degree) - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)
    p.ChangeDutyCycle(dc)

def cleanup():
    p.stop()
    GPIO.cleanup()

init()

root = Tk()
root.title("Servo")
root.geometry("300x50")

degSlider = Scale(root, label = "Steering", length = 200, orient = 'h', from_ = -180.0, to = 180.0, showvalue = False, command = convert_dc)

degSlider.pack()

root.mainloop()

cleanup()

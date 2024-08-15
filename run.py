from blinker import Device
from blinker.voice_assistant import VoiceAssistant, VAType, AliLightMode, PowerMessage, ModeMessage, ColorMessage, \
    ColorTempMessage, BrightnessMessage, DataMessage

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import random

GPIO.setmode(GPIO.BCM)

def generate_data():
    return random.randint(1, 100)


async def realtime_func(keys):
    print("realtime func received {0}".format(keys))
    for key in keys:
        if key == "humi":
            await device.sendRtData(key, generate_data)
        elif key == "temp":
            await device.sendRtData(key, generate_data)

device = Device("ec4369c659bc", realtime_func=realtime_func)


if __name__ == '__main__':
    device.run()

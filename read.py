# This Python file uses the following encoding: utf-8
import serial, time

ser = serial.Serial('/dev/ttyUSB0', 9600)

for b in range(256):
    time.sleep(0.1)  # Короткая пауза
    print(ser.read_all().hex())


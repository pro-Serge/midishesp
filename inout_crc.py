# This Python file uses the following encoding: utf-8
import serial, time

ser = serial.Serial('/dev/ttyUSB0', 9600)

test_packet1 = ("55 0D 01 02 03 00 00 00 00 00 00 00 00 00 00 00")
packet1 = bytearray.fromhex(test_packet1)
crc1 = sum(packet1[2:15])
packet1[15] = crc1 & 0xFF;
print("Отправил:",f"{packet1.hex()}")

ser.write(bytes(packet1))

time.sleep(0.1)  # Короткая пауза
print("Ответ 1 :",ser.read_all().hex())

time.sleep(2.1)  # Длинная пауза
print("Ответ 2 :",ser.read_all().hex())


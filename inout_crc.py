# This Python file uses the following encoding: utf-8
import serial, time

ser = serial.Serial('/dev/ttyUSB0', 9600)

test_packet1 = ("55 0D 00 05 00 00 00 00 00 00 00 00 00 00 00 00")
packet1 = bytearray.fromhex(test_packet1)
crc1 = sum(packet1[2:15])
packet1[15] = crc1 & 0xFF;
print("Отправил:",f"{packet1.hex()}")
ser.write(bytes(packet1))

time.sleep(0.2)  # Короткая пауза
print("Ответ 1 :",ser.read_all().hex())

time.sleep(0.1)  # Короткая пауза

test_packet2 = ("55 0D 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
packet2 = bytearray.fromhex(test_packet2)
crc2 = sum(packet2[2:15])
packet2[15] = crc2 & 0xFF;
print("Отправил:",f"{packet2.hex()}")
ser.write(bytes(packet2))


time.sleep(0.2)  # Короткая пауза
print("Ответ 1 :",ser.read_all().hex())


time.sleep(2.1)  # Длинная пауза
print("Ответ 2 :",ser.read_all().hex())

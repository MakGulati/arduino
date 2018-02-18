import serial
import time
ArduinoSerial=serial.Serial('/dev/cu.usbmodem14611',9600)
time.sleep(2)
var = input("you entered: ") #get input from user

     
if (var == '1'): #if the value is 1
    ArduinoSerial.write('1'.encode()) #send 1
    print ("LED turned ON")
    time.sleep(1)

if (var == '0'): #if the value is 0
    ArduinoSerial.write('0'.encode()) #send 0
    print ("LED turned OFF")
    time.sleep(1)
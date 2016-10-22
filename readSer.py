import sys
import serial
import datetime

FILE = open('temp.txt', 'a')
try:
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    print "USB0"
except:
    ser = serial.Serial('/dev/ttyUSB1', 115200)
    print "USB1"

while 1:
    n = datetime.datetime.now()
    t = ser.readline()
    sys.stdout.write(t)
    FILE.write(str(n))
    FILE.write(' ')
    FILE.write(str(t))

import os
CPU = "m328pb"
PROGTYPE = "arduino"
PROGLOCATION = "/dev/ttyUSB0"
BAUD = "115200"
PROJECTLOCATION = "/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/project.hex"

UploadString = "sudo avrdude -p " + CPU + " -c " + PROGTYPE + " -P " + PROGLOCATION +" -b " + BAUD + ' -U flash:w:' + PROJECTLOCATION
print(UploadString)
os.system(UploadString)
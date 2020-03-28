import MegaforceAVR as Megaforce
FILELOCATIONS = ['/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/main.c',
                     '/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/MMINIT.c',
                     '/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/systime.c']
CPU = "atmega328pb"
Megaforce.Compile(CPU,FILELOCATIONS)

CPUTYPE = "m328pb"
PROGTYPE = "arduino"
PROGLOCATION = "/dev/ttyUSB0"
BAUD = "115200"
PROJECTLOCATION = "/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/project.hex"
Megaforce.Upload(CPUTYPE,PROGTYPE,PROGLOCATION,BAUD,PROJECTLOCATION)
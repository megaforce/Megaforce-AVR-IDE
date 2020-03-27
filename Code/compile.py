import os
CPU = "atmega328pb"
CompileString = ""
FILENAMES = []
COMPILEFILES = [];
FILELOCATIONS = ['/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/main.c',
                 '/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/MMINIT.c',
                 '/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/systime.c']

PROJECTLOCATION = "";
for i in range (0,len(FILELOCATIONS)):
    FILENAMES.append((os.path.basename(FILELOCATIONS[i])))

PROJECTLOCATION = os.path.abspath(FILELOCATIONS[0])
PROJECTLOCATION = PROJECTLOCATION.replace(FILENAMES[0],'project.elf')

for i in range(0,len(FILELOCATIONS)):
    tmp = FILELOCATIONS[i]
    tmp = tmp[:-1] + 'o'
    COMPILEFILES.append(tmp)

for i in range(0,len(FILELOCATIONS)):
    CompileString = 'avr-gcc -c -mmcu=' + CPU + ' -o '  + COMPILEFILES[i] + ' ' + FILELOCATIONS[i]
    os.system(CompileString)

LinkString = "avr-gcc -mmcu=" + CPU + " -o "

for i in range(0,len(FILELOCATIONS)):
    LinkString += COMPILEFILES[len(FILELOCATIONS)- 1 - i] + " "

LinkString += " -o " + PROJECTLOCATION


HexString = "avr-objcopy -O ihex -j .text -j .data " + PROJECTLOCATION + " " +  PROJECTLOCATION.replace('project.elf','project.hex')

os.system(LinkString)
os.system(HexString)
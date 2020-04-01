import subprocess
import shlex
import os
import ConfigHandler as handler
def Compile(projectConfigLocation):
    if not projectConfigLocation:
        return 123
    Lookup = ["CPU =","FILELOCATIONS ="]
    Configdata = handler.GetConfigData(Lookup)
    #FILELOCATIONS =['/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/main.c' ,
    #'/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/MMINIT.c',
    #'/home/patricija/Namizje/AVR/PortManipulation/PortManipulation/systime.c']
    CPU = Configdata [0]
    FILELOCATIONS = Configdata[1]

    # These are the files needed to store vital information for the parsing of the compile command
    CompileString = ""
    FILENAMES = []
    COMPILEFILES = [];
    PROJECTLOCATION = "";

    for i in range (0,len(FILELOCATIONS)):
        FILENAMES.append((os.path.basename(FILELOCATIONS[i]))) # Stores the names of .c files in this array

    PROJECTLOCATION = os.path.abspath(FILELOCATIONS[0]) # Stores the path to the first .c file
    PROJECTLOCATION = PROJECTLOCATION.replace(FILENAMES[0],'project.elf')   # changes the .c file into project.elf
    # This is done to generate project.elf file in the same location as the first .c file
    # Note that the first .c file is not effected by this action

    for i in range(0,len(FILELOCATIONS)):
        tmp = FILELOCATIONS[i] # Fetches the path to a .c file and stores it into a temporary file
        tmp = tmp[:-2] + 'o' # Changes the files type from .c to .o (ONLY IN A STRING, NOT ON ACTUAL FILE)
        COMPILEFILES.append(tmp) # Appends the previously edited string into an array


    if len(FILELOCATIONS) == 1:
        PROJECTLOCATION = PROJECTLOCATION.replace('project.elf','project.hex')
        CompileString = 'avr-gcc -c -mmcu=' + CPU + ' -o  ' +PROJECTLOCATION   + ' ' + FILELOCATIONS[i] # Generates the compile command for the current file
        proc = subprocess.Popen(shlex.split(CompileString), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()  # Runs the compile command
        print(out)
        print(err)

    elif len(FILELOCATIONS) > 1:
        for i in range(0, len(FILELOCATIONS)):
            CompileString = 'avr-gcc -c -mmcu=' + CPU + ' -o ' + COMPILEFILES[i] + ' ' + FILELOCATIONS[i]  # Generates the compile command for the current file
            print(CompileString)
            proc = subprocess.Popen(shlex.split(CompileString), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()  # Runs the compile command
            print(out)
            print(err)

        LinkString = "avr-gcc -mmcu=" + CPU + " -o " # Header of the link command

        for i in range(0,len(FILELOCATIONS)):
            LinkString += COMPILEFILES[len(FILELOCATIONS)- 1 - i] + " " # Appends the file locations of the compiled files (.o)

        LinkString += " -o " + PROJECTLOCATION # Appends the the file with the location of the project.elf file

        # Converts project.elf into project.hex
        HexString = "avr-objcopy -O ihex -j .text -j .data " + PROJECTLOCATION + " " + PROJECTLOCATION.replace('project.elf','project.hex')

        print (LinkString)
        print(HexString)
        # Runs the link command
        proc = subprocess.Popen(shlex.split(LinkString), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        print(out)
        print(err)
        # Runs the convert command
        proc = subprocess.Popen(shlex.split(HexString), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        print(out)
        print(err)
    else:
        print("NO FILES SELECTED!")



def Upload(projectConfigLocation):
    if not projectConfigLocation:
        return 123
    Lookup = ["CPUTYPE =", "PROGTYPE =","PROGLOCATION =","BAUD =","PROJECTLOCATION ="]
    Configdata = handler.GetConfigData(Lookup)
    CPUTYPE = Configdata[0]
    PROGTYPE = Configdata[1]
    PROGLOCATION = Configdata[2]
    BAUD = Configdata[3]
    PROJECTLOCATION = Configdata[4]

    # Generation of the upload script for avrdude
    # It has to be run with sudo otherwise the command might not be permited to execute
    UploadString = "sudo avrdude -p " + CPUTYPE + " -c " + PROGTYPE + " -P " + PROGLOCATION + " -b " + BAUD + ' -U flash:w:' + PROJECTLOCATION
    # Runs the upload script
    proc = subprocess.Popen(shlex.split(UploadString), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    print(out)
    print(err)


def TestBoard(projectConfigLocation):
    if not projectConfigLocation:
        return 123
    TestString = "sudo avrdude -p " + CPUTYPE + " -c " + PROGTYP
    E + " -P " + PROGLOCATION + " -b " + BAUD
    # Runs the upload script
    proc = subprocess.Popen(shlex.split(TestString), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    print(out)
    print(err)




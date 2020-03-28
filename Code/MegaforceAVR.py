import os
def Compile(CPU,FILELOCATIONS):
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
        tmp = tmp[:-1] + 'o' # Changes the files type from .c to .o (ONLY IN A STRING, NOT ON ACTUAL FILE)
        COMPILEFILES.append(tmp) # Appends the previously edited string into an array

    for i in range(0,len(FILELOCATIONS)):
        CompileString = 'avr-gcc -c -mmcu=' + CPU + ' -o '  + COMPILEFILES[i] + ' ' + FILELOCATIONS[i] # Generates the compile command for the current file
        os.system(CompileString) # Runs the compile command

    LinkString = "avr-gcc -mmcu=" + CPU + " -o " # Header of the link command

    for i in range(0,len(FILELOCATIONS)):
        LinkString += COMPILEFILES[len(FILELOCATIONS)- 1 - i] + " " # Appends the file locations of the compiled files (.o)

    LinkString += " -o " + PROJECTLOCATION # Appends the the file with the location of the project.elf file

    # Converts project.elf into project.hex
    HexString = "avr-objcopy -O ihex -j .text -j .data " + PROJECTLOCATION + " " + PROJECTLOCATION.replace('project.elf','project.hex')

    # Runs the link command
    os.system(LinkString)
    # Runs the convert command
    os.system(HexString)


def Upload(CPUTYPE,PROGTYPE,PROGLOCATION,BAUD,PROJECTLOCATION):
    # Generation of the upload script for avrdude
    # It has to be run with sudo otherwise the command might not be permited to execute
    UploadString = "sudo avrdude -p " + CPUTYPE + " -c " + PROGTYPE + " -P " + PROGLOCATION + " -b " + BAUD + ' -U flash:w:' + PROJECTLOCATION
    # Runs the upload script
    os.system(UploadString)

def TestBoard(CPUTYPE,PROGTYPE,PROGLOCATION,BAUD):
    TestString = "sudo avrdude -p " + CPUTYPE + " -c " + PROGTYPE + " -P " + PROGLOCATION + " -b " + BAUD
    # Runs the upload script
    os.system(TestString)
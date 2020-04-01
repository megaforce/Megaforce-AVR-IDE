import unicodedata
def GetConfigData(Lookup):
    f = open("programFile.txt","r")
    projectConfigLocation = f.read()
    f.close()
    tmp = []
    string = ""
    f = open(projectConfigLocation, 'r')
    config = f.read()

    for i in range (0 ,len(Lookup)):
        endterminator = "END" + Lookup[i]
        for j in range ((config.find(Lookup[i]) + len(Lookup[i])),config.find(endterminator[:-2])-1):
                string += config[j]

        if(Lookup[i] == "FILELOCATIONS ="):
            string = string.split("\n")

        tmp.append(string)
        string = ""

    return(tmp)

def BuildConfigFile(CPU,FILELOCATIONS,CPUTYPE,PROGTYPE,PROGLOCATION,BAUD):
    f = open("programFile.txt", "r")
    projectConfigLocation = f.read()
    f.close()
    tmp = FILELOCATIONS.split("\n")
    tmp2 = []
    print(FILELOCATIONS)
    string = ""
    for i in range (0,len(tmp)):
        if (len(tmp[i]) > 1):
            tmp[i] = tmp[i].replace('?', '')
            tmp[i] = tmp[i].replace('#', '')
            tmp[i] = tmp[i].replace(' ', '')
            tmp2.append(tmp[i])

    FILELOCATIONS = tmp2
    strCPU = "CPU ="+CPU+"#ENDCPU"
    for i in FILELOCATIONS:
        string += i +"\n"
    string = string [:-2]
    strFILELOCATIONS = "FILELOCATIONS ="+ string +"#ENDFILELOCATIONS"
    strCPUTYPE = "CPUTYPE ="+ CPUTYPE +"#ENDCPUTYPE"
    strPROGTYPE = "PROGTYPE ="+ PROGTYPE +"#ENDPROGTYPE"
    strPROGLOCATION = "PROGLOCATION ="+ PROGLOCATION +"#ENDPROGLOCATION"
    strBAUD = "BAUD ="+ BAUD +"#ENDBAUD"
    strPROJECTLOCATION = "PROJECTLOCATION ="+ "/home/patricija/Namizje/AVR/Test/project.hex" +"#ENDPROJECTLOCATION"
    insert = strCPU + "\n" + strFILELOCATIONS + "\n" + strCPUTYPE + "\n" + strPROGTYPE + "\n" + strPROGLOCATION + "\n" + strBAUD + "\n" + strPROJECTLOCATION + "\n"
    print(insert)
    f = open(projectConfigLocation,"w")
    f.write(insert)
    f.close()



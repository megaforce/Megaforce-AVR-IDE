def GetConfigData(Lookup,projectConfigLocation):
    tmp = []
    string = ""
    f = open(projectConfigLocation, 'r')
    config = f.read()
    for i in range (0,len(Lookup)):
        endterminator = "END" + Lookup[i]
        for j in range ((config.find(Lookup[i]) + len(Lookup[i])),config.find(endterminator[:-2])-1):
                string += config[j]
        print(string)
        tmp.append(string)
        string = ""
    return(tmp)

def EditConfig(Changes,projectConfigLocation):
    return("Hello")
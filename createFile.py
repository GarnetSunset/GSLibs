def createFile(fileName):
    global flNm
    if(os.path.isfile(fileName)):
        with open(fileName, 'r') as myfile:
            flNm=myfile.read().replace('\n', '')
    else:
        flNm = input("Type the Server URL\n> ")
        flNmfile = open(fileName, "w")
        flNmfile.write(flNm)
        flNmfile.close()

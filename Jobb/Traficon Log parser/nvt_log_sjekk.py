readlist = []
with open("TraficonLog.txt", "r") as fh:
    #fh.close()
    print("Opened fh")
    readlist.append(fh.readlines())
    print("readlist.append(fh.readlines())")
    fh.close()
##    for line in fh:
##        lines = fh.readline()
##        readlist.append(line)
print(readlist)

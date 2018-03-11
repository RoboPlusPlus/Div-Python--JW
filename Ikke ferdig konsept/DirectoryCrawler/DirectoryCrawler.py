import os
import time
import io

last_directory_scan_logFile_name = "last_dir_scan.txt"
last_file_scan_logFile_name = "last_file_scan.txt"

root_directories = [b'C:\Users\JoachimR\Dropbox\Programmering Div\Python']

scanned_directories = set()

def makeFile(_fileName):
    with open(_fileName, "w") as fh:
        fh.close()
    print("File created with name {}".format(_fileName))

def list_from_textFile(_filename):
    _dir_list = []
    with open(_filename, "r") as fh:
        for line in fh:
            _dir_list.append(line)

    print("list loaded from text file {}, with {} lines".format(_filename, len(_dir_list)))
    return _dir_list

def scan_directories(rootDir):
    _directories_found = []
    _files_found = []

    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        _directories_found.append(str(dirName))
        for fname in fileList:
            #print('\t%s' % fname)
            _files_found.append(str(fname))

    return _directories_found, _files_found

def save_list_to_file(_full_file_path, _list_to_save):
    if os.path.isfile(_full_file_path):
        with open(_full_file_path, "w") as fh:
            for entry in _list_to_save:
                fh.writelines(entry)
                fh.write("\n")
            writeSuccess = True
    else:
        writeSuccess = False
    return writeSuccess


tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.localtime()
saveName = "dirScan{}_{}_{}_{}_{}_{}.txt".format(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec)
print(saveName)

def run():
    #Sjekker om loggfiler eksisterer
    if not os.path.isfile(last_directory_scan_logFile_name):
        makeFile(last_directory_scan_logFile_name)
    if not os.path.isfile(last_file_scan_logFile_name):
        makeFile(last_file_scan_logFile_name)

    #Laster inn data fra forrige scan
    list_from_textFile(last_directory_scan_logFile_name)
    list_from_textFile(last_file_scan_logFile_name)


    for directory in root_directories:
        directories_found, files_found = scan_directories(directory)
        print(directories_found)
        print(files_found)
        print(type(directories_found[0]))

        save_list_to_file(last_directory_scan_logFile_name, directories_found)
        save_list_to_file(last_file_scan_logFile_name, files_found)

run()


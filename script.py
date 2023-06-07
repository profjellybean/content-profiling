import sys
import os
from subprocess import Popen
from zipfile import ZipFile

# path to fits.bat, adjust as needed
pathToFits = r"C:/Users/valen/Desktop/fits-1.6.0"

dir = sys.argv[1]
outputDir = dir.split('\\')
outputDir = outputDir[0: len(outputDir) - 1]
outputDir = '\\'.join(outputDir)

# if more than one argument is given, print error message and exit
if (len(sys.argv) > 2 or len(sys.argv) < 1):
    print("Wrong number of arguments, please provide one argument: the directory to be processed")
    exit(1)

try:
    # create output directory inside the given directory
    os.makedirs(outputDir + '/output/')
except OSError:
    # if directory already exists, print error message
    print("Creation of the directory %s failed, already existing" % dir)

entries = os.listdir(dir)
for entry in entries:
    if (entry.endswith(".zip")):  # if zip file is found, extract it
        with ZipFile(dir + "/" + entry, 'r') as zObject:
            zObject.extractall(dir)


p = Popen("fits.bat -i " + dir + " -r -o " + outputDir + "/output/",
          cwd=pathToFits, shell=True)  # run fits.bat with the given directory as input
stdout, stderr = p.communicate()

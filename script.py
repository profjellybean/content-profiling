import sys
import os
from subprocess import Popen
from zipfile import ZipFile


dir = sys.argv[1]

if (len(sys.argv) > 2):
    print("Too many arguments")
    exit(1)

try:
    os.makedirs(dir + '/output/')
except OSError:
    print("Creation of the directory %s failed" % dir)

entries = os.listdir(dir)
for entry in entries:
    if (entry.endswith(".zip")):
        with ZipFile(dir + "/" + entry, 'r') as zObject:
            zObject.extractall(dir)


p = Popen("fits.bat -i " + dir + " -r  -o " + dir + "/output/",
          cwd=r"C:/Users/valen/Desktop/fits-1.5.1", shell=True)
stdout, stderr = p.communicate()

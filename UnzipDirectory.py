import os,zipfile,time
import multiprocessing as mp
import itertools
import traceback
from os import listdir
import os
from os.path import isfile, join, exists
import sys
from  shutil import *
import glob
from itertools import *
from Parse import *
import time 
from duplicity.dup_temp import TempPath
import contextlib



# pool = mp.Pool(processes= 3)


# pool.map(unzip)
# results = pool.map(unzip)
# tempPath = '/home/temp/'
# os.mkdir(tempPath)
zipfiles = []
datfiles = []
mypath = sys.argv[1]

newDirectory = mypath + "temp"
if os.path.exists(newDirectory):
    rmtree(newDirectory)
    os.makedirs(newDirectory)
    
######## lista fisiere
for dirpath, subdirs, files in os.walk(mypath):
    for x in files:
        if x.endswith(".zip"):
            zipfiles.append(os.path.join(dirpath, x))



def unZipWrapped(unZip, zipFileName, newDirectory):
    try:
      
        unZip((zipFileName, newDirectory))
    except:
        print('%s: %s' % (zipFileName, traceback.format_exc()))

# def unZip_forMap((zipFileName, newDirectory)):
    start_time = time.time()
    head, tail = os.path.split(zipFileName)
   # newDir = newDirectory + "_".join(head.split('/')) + '_' + tail[:-4]
    
    newDir = newDirectory +  tail[:-4]
    os.mkdir(newDir)
    # print zipfile
    fh = open(zipFileName)
    try:
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            outpath = newDir
            z.extract(name, outpath)
        fh.close()

    except :
        print'---------------------------------------------------',  z
        # os.mkdir("_".join(head.split('/')))
    print zipFileName + "deschis in " + str(time.time() - start_time)

def unZip((zipFileName, tempPath)):
    start_time = time.time()
    head, tail = os.path.split(zipFileName)
    #newDir = tempPath + "_".join(head.split('/')) + '_' + tail[:-4]
    
    newDir = tempPath +"_" +  tail[:-4]
    os.mkdir(newDir)
    outpath = newDir

#     fh = open(zipFileName)

    if zipfile.is_zipfile(zipFileName):
        with contextlib.closing(zipfile.ZipFile(zipFileName, "r")) as z:                
                try:
                    z.extractall(outpath)
                except (zipfile.BadZipfile, zipfile.LargeZipFile), e:
                    pass
            
                
    
#     try:
#         z = zipfile.ZipFile(fh)
# #         with contextlib.closing(zipfile.ZipFile('test.zip', "r")) as z:
# #             z.extractall(outpath)
#         for name in z.namelist():
# 
#             z.extract(name, outpath)
# #             
#         fh.close()
# 
#     except :
#         print'---------------------------------------------------',  z
#         # os.mkdir("_".join(head.split('/')))
#     finally:
# 
#         fh.close()
#     print zipFileName + "deschis in " + str(time.time() - start_time)

print "numarul de fisiere de dezarhivat" + str(len(zipfiles))
  
def main():
    pool = mp.Pool(processes= 3)
    start_time = time.time()
#     print len(zipfiles)
    
    pool.map(unZip, zip(zipfiles, itertools.repeat(newDirectory, len(zipfiles))))
    
    for dirpath, subdirs, files in os.walk(mypath):
        for x in files:
            if x.endswith("memorie1.dat"):
                datfiles.append(os.path.join(dirpath, x))
    print 'ok de la unzipare'
#     start_time = time.time()
#     for datFile in datfiles:
#         try:
#             parsefile(datFile)
#         except Exception as e:
#             print e
#             
            
#     print len(datfiles)
#     pool.map(parsefile, datfiles)

    q = [pool.apply_async(parsefile, args = (f,"csv",  )) for f in  datfiles]
    pool.close()
    pool.join()
    
    jsonfiles = []
    for dirpath, subdirs, files in os.walk(mypath):
        for x in files:
            if x.endswith("memorie1.csv"):
                jsonfiles.append(os.path.join(dirpath, x))
    print "finished csving " + str(len(zipfiles)) + " from " + str(len(jsonfiles))
#     print "################Timpul total :",  time.time() - start_time
#     print time.time() - start_time


if __name__ == "__main__":
    main()
    


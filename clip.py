from os import listdir
import os
from os.path import isfile, join, exists
import zipfile
import sys
from  shutil import *
import glob
from itertools import *
from Parse import *
import time 




import zipfile
from zipfile import BadZipfile


outfile = "/home/mihai/ArhivaDateLema/somedata/temp/data2.json"

mypath = sys.argv[1]
# print mypath
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print onlyfiles

def check_is_zipfile(filePath):
    if filePath.endswith(".zip"):
        return filePath

only_zip_files = filter(check_is_zipfile, onlyfiles)
newDirectory = mypath + "temp"

if os.path.exists(newDirectory):
    rmtree(newDirectory)
    os.makedirs(newDirectory)
    
else:os.makedirs(newDirectory)
    
##parallel unzip 
for zipFile in only_zip_files:
    fh = open(mypath + "/" + zipFile, 'rb')
    z = zipfile.ZipFile(fh)
    name  = "memorie1.dat"
    if  name  in z.namelist():
       
        try:
            newSubDirectory = newDirectory  +"/"+ zipFile[:-4]
            os.makedirs(newSubDirectory)
            z.extract(name, newSubDirectory)
        except BadZipfile:
            continue        
    fh.close()
    

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)   if os.path.isdir(os.path.join(a_dir, name))]


myFiles = []
for subdir in get_immediate_subdirectories(newDirectory):   
    newPath = join(newDirectory , subdir)
    myFiles.append( glob.glob(newPath +"/*.dat"))


start_time = time.time() 
for file in  list(chain.from_iterable(myFiles)):
# #     print file
    parsefile(file, outfile)
    
    
    
# import multiprocessing as mp
# pool = mp.Pool(processes=4)
# # [pool.apply(parsefile, args = (f,outfile))
# 
# results = pool.map((lambda f : parsefile(f, outfile)) , list(chain.from_iterable(myFiles)))
# 
# 
# 
#    
# # filename = parsefile(list(chain.from_iterable(myFiles))[1], outfile)
# 
# time_spended = time.time() - start_time
# print "timp executie : ",  time_spended, "secunde"

# sc = SparkContext()      
# sqlContext  = SQLContext(sc)
#  
# df = sqlContext.read.format("json").load(filename)
# 
# df.registerTempTable("frames")
# inp_num= sqlContext.sql("SELECT inp_num from frames")
# print inp_num
# df.select("stare_drv").show()
# parse_file("/home/mihai/ArhivaDateLema/memorie1.dat")



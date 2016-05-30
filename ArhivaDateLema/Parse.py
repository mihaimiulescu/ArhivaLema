###### Pozitii ale marimilor in fisierul binar

from bitstring import *
from MathHelperFunctions import *
from ValuesFactory  import *
import json
from pyspark.sql import SQLContext
from pyspark.sql.context import SQLContext
from pyspark.context import SparkContext
# from src.clip import outfile
import os

class CorruptFileError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
 

def write_chunk_toFile(chunk, outFile, type_of_file = "json"):
    if (type_of_file == "json" ):
        outFile.write("{}\n".format(json.dumps(chunk)))
    
    
######Testez fisierul daca este corupt############  
def  WrappedConstBitStream(filename  = file):
    try:
        s = ConstBitStream(filename = filename)
        if  s.startswith('0xf5fe') != True:
            raise  Exception('spam')
        foundF5FE = s.find('0xf5fe', bytealigned=True)
        foundF5F6 = s.find('0xf6f5', bytealigned=True)
        diff = foundF5F6[0] - foundF5FE[0]
        if diff != 3104:
            raise ValueError('Fisier Corupt')  
        #Exception('fisier corupt diferenta aiurea')
#             s.pos = foundF5FE[0]
#         else:
#             print "Fisierul este corupt!"
        return s ## trebuia intr-un else 
        
    except IOError:
        print "Fisierul nu poate fi deschis ioerror!"
#     except 'fisier corupt':
#         print "Fisierul nu poate fi deschis"
    
    
def parsefile(file, type_of_file_out = "json"): 
    
    
  
#     try:
#         s = WrappedConstBitStream(filename = file)
# #         s = ConstBitStream(filename=file)
#         
#     except IOError:
#         print "Fisierul nu poate fi deschis!"
#     try:
    s = WrappedConstBitStream(filename = file)
#     except Exception as e:
#         pass
    
        
#     outfile = open('/home/mihai/ArhivaDateLema/somedata/temp/data2.json', 'a+')
    
#     outfile = open(outfileName, 'a+')
    if (type_of_file_out == "json"):
        outfilename = os.path.dirname(file) + "/memorie1.json"
    elif (type_of_file_out == "csv"):
        outfilename = os.path.dirname(file) + "/memorie1.csv"
        
    outFile = open(outfilename, 'a+')
    print "starting "+ outfilename + "................."
    
    
    
#     if s.startswith('0xf5fe') != True:
#     
#         break
#         print "Fisierul este corupt!"
#     else:
#         print "ok"
#     try:
#         
#         foundF5FE = s.find('0xf5fe', bytealigned=True)
#         foundF5F6 = s.find('0xf6f5', bytealigned=True)
#         diff = foundF5F6[0] - foundF5FE[0]
#     except "fisier corupt":
#         print 'fisier corupt'
#     else:
#     
#         if diff == 3104:
#             s.pos = foundF5FE[0]
#         else:
#             print "Fisierul este corupt!"
    foundF5FE = s.find('0xf5fe', bytealigned=True)       
    s.pos = foundF5FE[0]
        
    s.pos = 8 ##skip F5
        
    Boxuri = InitializeBox3_Box8()
        
    while 1: 
        a = s.readlist('hex:2032, hex:512, hex:264, hex:168, hex:120')  
            
        icol = a[0]
        icsa = a[1]
        ivms = a[2]
        gps  = a[3]
        imto = a[4]
            
            
        icol_values = GetValuesFromIcol(icol, Boxuri, type_of_file_out) # intoarce un dictionar 
        
                
        try:
            s.pos = s.pos +16
        except ValueError:
            break
        
        #     
        #     if 'def_drv1' in Ceta['S1'].keys():
        #         print Ceta['S1']['def_drv1']['UM']
    #         json.dump(icol_values, outfile, indent = 2)
        write_chunk_toFile(icol_values,outFile)
        #outFile.write("{}\n".format(json.dumps(icol_values)))
            
    outFile.close()
    return outFile.name 

    
      
     
         
# sqlContext.read.format("json").load("/home/mihai/ArhivaDateLema/somedata/temp/data2.json")
    










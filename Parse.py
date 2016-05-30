###### Pozitii ale marimilor in fisierul binar

from bitstring import *
from MathHelperFunctions import *
from ValuesFactory  import *
import json
import csv
import sys
import time
# from pyspark.sql import SQLContext
# from pyspark.sql.context import SQLContext
# from pyspark.context import SparkContext
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
    
    
  

    s = WrappedConstBitStream(filename = file)

    if (type_of_file_out == "json"):
        outfilename = os.path.dirname(file) + "/memorie1.json"
    elif (type_of_file_out == "csv"):
        outfilename = os.path.dirname(file) + "/memorie1.csv"
        
        
    
    outFile = open(outfilename, 'a+')
    
    header = []
    writer = csv.DictWriter(outFile, fieldnames = header)
#     writer = csv.DictWriter(outFile)
    
    print "starting "+ outfilename + "................."
    
    start_time = time.time()

    foundF5FE = s.find('0xf5fe', bytealigned=True)       
    s.pos = foundF5FE[0]
        
    s.pos = 8 ##skip F5
        
    Boxuri = InitializeBox3_Box8()
    header_counter = True #flag care spune daca este header sau nu (doar prima oara)
    
     
    while 1: 
        
#         a = s.readlist('hex:2032, hex:512, hex:264, hex:24,  hex:168, hex:96')  
        a = s.readlist('hex:2032, hex:512, hex:96, hex:24,  hex:168, hex:264')

           
        icol = a[0]
        icsa = a[1]
        ivms = a[2]
        offset = a[3]
        gps  = a[4]
        ivms = a[5]
            
            
        icol_values = GetValuesFromIcol(icol, Boxuri, type_of_file_out) # intoarce un dictionar 
        gps_values = GetValuesFromGPS(gps, type_of_file_out)
                
        try:
            s.pos = s.pos +16 #incerc sa sar peste f6f5 si apoi citesc iar 387 octeti  
        except ValueError:
            break
        

                #write_chunk_toFile(icol_values,outFile)
        
        
        row = {}
         
        for key in sorted(icol_values.iterkeys()):
      
            valoare = icol_values[key]
             
            if 'val' in valoare.keys():
                if type(valoare['val']) is list:
                    for k in xrange(len(valoare['val'])):
                        new_key = key + "_S" + str(k+1)
                        if (header_counter):
                            header.append(new_key)
                        row[new_key] = valoare['val'][k]
                else:
                    if (header_counter):
                        header.append(key)
                    row[key] = valoare['val']                   
                      
            else:               
                for k,v in valoare.items():                  
                    new_key = key + "_" + k
                    new_value = v
                    if (header_counter):
                        header.append(new_key)
                    row[new_key] = v
                     
 
                 
                 
#         if (header_counter == True):
#             header.extend(['p_cat','p_sa', 'data_lente', 'temp_trafo', 'mansa1_numerice', 'mansa1_forta',\
#                             'mansa1_viteza', 'mansa2_numerice', 'mansa2_forta','mansa2_viteza','defect0',\
#                              'defect1_lente','defect2_lente','defect3_lente','defect4_lente','defect5_lente','defect6_lente', 'defect7_lente', 'defect8_lente', \
#                              'defect9_lente', 'defect10_lente', 'defect11_lente', 'defect12_lente', 'defect13_lente', 'defect14_lente', 'defect15_lente','defect16_lente',\
#                               'defect17_lente', 'defect18_lente', 'defect19_lente', 'defect20_lente', 'defect21_lente', 'defect22_lente', 'defect23_lente','rezerva_lente'])
 
                         
#             writer.writeheader()
#             header_counter = False
       
       
        
#         row = {}
#         header   = ['data', 'loco']
        if (header_counter == True):                     
            header.extend(['data_gps', 'latitudine', 'longitudine', 'altitudine', 'curs', 'viteza_gps'])
            
        for key in sorted(gps_values.iterkeys()):     
            row[key] = gps_values[key]
        
        if (header_counter == True):
            
            writer.writeheader()
            header_counter = False
                
        try:
            writer.writerow(row)
        except csv.Error as e:
            print "Unexpected error:", sys.exc_info()[0]
            break
#         writer.writerow(row)
        
        #outFile.write("{}\n".format(json.dumps(icol_values)))
            
    outFile.close()
    print "################Timpul total pentru " + outfilename + "..." ,  time.time() - start_time

    return outFile.name 

    
      
     
         

    










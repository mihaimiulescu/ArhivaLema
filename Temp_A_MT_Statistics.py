from pyspark import SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.context import SQLContext, HiveContext
from pyspark.context import SparkContext
from pyspark.sql.functions import explode, least
from decimal import Decimal
from pyspark.sql.types import *


import json
from chardet.latin1prober import UDF
from types import NoneType

from pyspark.mllib.stat import Statistics
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np


conf = SparkConf().setMaster("local").setAppName("My application").set("spark.executor.memory", "1g")
sc = SparkContext()

# sc = SparkContext(conf=conf)      
sqlContext  = HiveContext(sc)
 
df = sqlContext.read.format("json").load("/home/mihai/ArhivaDateLema/somedata/temp/testDB.json")

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, BooleanType

import operator          
    

def is_value_in_marime(dict):
    d = dict.asDict()
    return "0x30" in d.values() 
        


def filtreaza_temperaturile_pe_tractiune(dict1,dict2):
    """ 
      primind 2 dictionare cauta in primul (cel cu ceta ) unde este tractiune , adica 0x30 sau 0x50 
      ia indicii si pe baza lor cauta maximul in al doilea
      deci ia in seama numai blocurile unde avem 0x30 sau 0x50
    """
    d_dict1 = dict1.asDict()
    d_dict2 = dict2.asDict()    
    indici = [k for k,v in d_dict1.items() if v in ['0x30']]
    
    for k,v in d_dict2.iteritems():
        if '0x30' not in d_dict1.values():
            return False
        if k in indici and v < 100 :
            return False 
        
    return True

def get_S1_value(dict1, bloc):
    d_dict1 = dict1.asDict()
    if d_dict1[bloc] > 100:
        return d_dict1[bloc] 
    else:
        return None

udfS1Value = udf(get_S1_value, DoubleType())

udfTempNumaiPeBlocurileInTractiune = udf(filtreaza_temperaturile_pe_tractiune,BooleanType())
   
udfFilterStareCeta = udf(is_value_in_marime, BooleanType())

print df.count()
from pyspark.sql.functions import *
from pyspark.sql.functions import concat, col, lit

table_filtered =  df.na.drop('any', subset = ["Temp_Aer_Mt.S1","Temp_Aer_Mt.S2", "Temp_Aer_Mt.S3", "Temp_Aer_Mt.S4", "Temp_Aer_Mt.S5", "Temp_Aer_Mt.S6"]).\
    filter(udfFilterStareCeta(df.Stare_Ceta)).\
    filter( (df.Temp_Aer_Mt.S1 > 0) & (df.Temp_Aer_Mt.S2 > 0) & (df.Temp_Aer_Mt.S3 > 0) & (df.Temp_Aer_Mt.S4 > 0) & (df.Temp_Aer_Mt.S5 > 0) & (df.Temp_Aer_Mt.S6 > 0) ).\
    filter(udfTempNumaiPeBlocurileInTractiune(df.Stare_Ceta, df.Temp_Mt1)).\
    withColumn("Temp_Mt1_S1", udfS1Value(df.Temp_Mt1, lit("S1"))).\
    withColumn("Temp_Mt1_S2", udfS1Value(df.Temp_Mt1, lit("S2"))).\
    withColumn("Temp_Mt1_S3", udfS1Value(df.Temp_Mt1, lit("S3"))).\
    withColumn("Temp_Mt1_S4", udfS1Value(df.Temp_Mt1, lit("S4"))).\
    withColumn("Temp_Mt1_S5", udfS1Value(df.Temp_Mt1, lit("S5"))).\
    withColumn("Temp_Mt1_S6", udfS1Value(df.Temp_Mt1, lit("S6"))).persist()


#    groupBy(df.Locomotiva).agg({ 'Temp_Mt1.S1': 'mean', 'Temp_Mt1.S2': 'mean', 'Temp_Mt1.S3': 'mean', 'Temp_Mt1.S4': 'mean', 'Temp_Mt1.S5': 'mean', 'Temp_Mt1.S6': 'mean'})
#                                 'Temp_Mt1.S3': 'mean','Temp_Mt1.S4': 'mean','Temp_Mt1.S5': 'mean','Temp_Mt1.S6': 'mean'} )
#     describe().toPandas()
#===============================================================================
# table_filtered =  df.na.drop('any', subset = ["Temp_Aer_Mt.S1","Temp_Aer_Mt.S2", "Temp_Aer_Mt.S3", "Temp_Aer_Mt.S4", "Temp_Aer_Mt.S5", "Temp_Aer_Mt.S6"]).\
#     filter(udfFilterStareCeta(df.Stare_Ceta)).\
#     filter( df.Temp_Aer_Mt.S1 > 100)
#    
#===============================================================================
  
# 
# table_filtered.filter(table_filtered.Temp_Mt1_S2 > 0).groupBy(df.Locomotiva).agg({ 'Temp_Mt1.S2': 'mean', }).show()
# table_filtered.filter(table_filtered.Temp_Mt1_S3 > 0).groupBy(df.Locomotiva).agg({ 'Temp_Mt1.S3': 'mean'}).show()
panda = table_filtered.toPandas()
pd_mean= panda.groupby('Locomotiva').describe().to_csv('/home/mihai/ArhivaDateLema/somedata/temp/temp_Mt1_Panda_Std_Report.csv')
# pd_mean= panda.groupby('Locomotiva').mean()

# # pd_mean.to_csv('/home/mihai/ArhivaDateLema/somedata/temp/temp_Mt1_Panda_Mean.csv')
# panda = panda.rename(columns={'Temp_Mt1_S1': 'a'})
# pd_std= panda.groupby('Locomotiva').std()
# pd_min= panda.groupby('Locomotiva').min()
# # pd_max= panda.groupby('Locomotiva').agg({'Temp_Mt1_S1', np.min})
# 
# 
# 
# pd = pd.concat((pd_mean, pd_std), axis = 1)
# # pd_std.to_csv('/home/mihai/ArhivaDateLema/somedata/temp/temp_Mt1_Panda_Std.csv')
# pd.to_csv('/home/mihai/ArhivaDateLema/somedata/temp/temp_Mt1_Panda_Std_Report.csv')

# table_filtered.filter(table_filtered.Temp_Mt1_S5 > 100).groupBy(table_filtered.Locomotiva).avg( 'Temp_Mt1.S5').show()

# table_filtered.registerTempTable("filtered")
# # results = sqlContext.sql("Select Locomotiva, Stare_ceta, Temp_Mt1, Temp_Mt1_S1,Temp_Mt1_S2,Temp_Mt1_S4,Temp_Mt1_S4,Temp_Mt1_S5,Temp_Mt1_S6  from filtered ").toPandas().to_csv('/home/mihai/ArhivaDateLema/somedata/temp/temp_aer_mt.csv')

# results = sqlContext.sql("Select *  from filtered ").toPandas()
# results.values

# .to_csv('/home/mihai/ArhivaDateLema/somedata/temp/temp_aer_mt.csv')

         



        
    

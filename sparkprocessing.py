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


conf = SparkConf().setMaster("local").setAppName("My application").set("spark.executor.memory", "1g")
sc = SparkContext()

# sc = SparkContext(conf=conf)      
sqlContext  = HiveContext(sc)
 
df = sqlContext.read.format("json").load("/home/mihai/ArhivaDateLema/somedata/temp/testDB.json")
# print df.count()

# a = df.filter(max(df['temp_apa_r']['S1'] , df['temp_apa_r']['S2']) > 1 ).count()





# df.select(df.data,df.bloc_soft.valoare).show()
# df.filter(df.temp_apa_r.S1 != '-').show()

# print  df.take(1)[0].asDict()
#     print k

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, BooleanType




import operator          

def remove_temps(x):    
    x_dict = x.asDict()
    return '-' in [v for v in x_dict.values()]
    
        
def return_values_from_bloc(x):
    x_dict = x.asDict()
    return x_dict.values()

def is_value_in_marime(dict):
    d = dict.asDict()
    return "0x30" in d.values() or "0x50" in d.values()
        
                
def get_maximum_bloc_cu_temp_apa_c(x):
    x_dict = x.asDict()
    del x_dict['UM']
   # x_dict = dict((k, map(float, v)) for k, v in x_dict.iteritems())
    return max(x_dict.iteritems(), key=operator.itemgetter(1))[0] 

def get_diff_max_min_marime_cu_blocuri(d):
    d_dict = d.asDict()
    del d_dict['UM']
    if  isinstance(min(d_dict.values() , NoneType) or isinstance(max(d_dict.values())), NoneType):
        return 0
    else:return round(max(d_dict.values()) - min(d_dict.values()),2)

def get_min_value_temp_apa_c(x):
    x_dict = x.asDict()
    del x_dict['UM']
    #x_dict = dict((k, map(float, v)) for k, v in x_dict.iteritems())
    if  isinstance(min(x_dict.values()) , NoneType): return 0
    else: return min(x_dict.values())  

def diff_max_min_pe_tractiune(dict1,dict2):
    """ 
      primind 2 dictionare cauta in primul (cel cu ceta ) unde este tractiune , adica 0x30 sau 0x50 
      ia indicii si pe baza lor cauta maximul in al doilea
      deci ia in seama numai blocurile unde avem 0x30 sau 0x50
    """
    d_dict1 = dict1.asDict()
    d_dict2 = dict2.asDict()
    indici = [k for k,v in d_dict1.items() if v in ['0x50', '0x30']]
    temperaturi_valide = [t for i,t in d_dict2.items() if i in indici]
    return round(max(temperaturi_valide) - min(temperaturi_valide),2)

def bloc_cu_max_pe_tractiune(dict1,dict2):
    """ 
      primind 2 dictionare cauta in primul (cel cu ceta ) unde este tractiune , adica 0x30 sau 0x50 
      ia indicii si pe baza lor cauta maximul in al doilea
      deci ia in seama numai blocurile unde avem 0x30 sau 0x50
    """
    d_dict1 = dict1.asDict()
    d_dict2 = dict2.asDict()    
    indici = [k for k,v in d_dict1.items() if v in ['0x50', '0x30']]
    temperaturi_valide = {i:t for i,t in d_dict2.items() if i in indici}
    return max(temperaturi_valide.iteritems(), key=operator.itemgetter(1))[0] 


udfBlocMaxTempApa =udf(get_maximum_bloc_cu_temp_apa_c, StringType())

udfBlocMaxNumaiPeBlocurileInTractiune = udf(bloc_cu_max_pe_tractiune,StringType())
udfDiffMaxMinNumaiPeBlocurileInTractiune = udf(diff_max_min_pe_tractiune, StringType()) #(df.Stare_Ceta, df.Temp_Apa_C, ))



udfMinTempApa =udf(get_min_value_temp_apa_c, StringType())
 

    
    
udfRemoveBadTemperatures = udf(remove_temps, BooleanType())
udfRetValues = udf(return_values_from_bloc, StringType())

udfDiffMaxMinBlocuri = udf(get_diff_max_min_marime_cu_blocuri, StringType())


udfFilterStareCeta = udf(is_value_in_marime, BooleanType())
# df.select(lambda s: udfs.temp_apa_r)
# df.withColumn("max_bloc_temp_apa_r", udfMaxTempApa(df.temp_apa_r)).show(10)
# df.filter(udfRemoveBadTemperatures(df.temp_apa_r)).show(10)
print df.count()
from pyspark.sql.functions import *

# table_filtered =  df.na.drop('any', subset = ["Temp_Apa_R.S1","Temp_Apa_R.S2", "Temp_Apa_R.S3", "Temp_Apa_R.S4", "Temp_Apa_R.S5", "Temp_Apa_R.S6"]).\
#     filter(udfFilterStareCeta(df.Stare_Ceta)).\
#     withColumn("temp_apa_r_max_bloc", udfBlocMaxTempApa(df.Temp_Apa_R)).\
#     withColumn("diff", udfDiffMaxMinBlocuri(df.Temp_Apa_R)).\
#     sort(asc("diff"))

# table_filtered =  df.na.drop('any', subset = ["Temp_Apa_R.S1","Temp_Apa_R.S2", "Temp_Apa_R.S3", "Temp_Apa_R.S4", "Temp_Apa_R.S5", "Temp_Apa_R.S6"]).\
#     filter(udfFilterStareCeta(df.Stare_Ceta)).\
#     withColumn("temp_apa_c_max_bloc", udfBlocMaxTempApa(df.Temp_Apa_C)).\
#     withColumn("diff", udfDiffMaxMinBlocuri(df.Temp_Apa_C)).\
#     sort(asc("diff"))


table_filtered =  df.na.drop('any', subset = ["Temp_Apa_C.S1","Temp_Apa_C.S2", "Temp_Apa_C.S3", "Temp_Apa_C.S4", "Temp_Apa_C.S5", "Temp_Apa_C.S6"]).\
    filter(udfFilterStareCeta(df.Stare_Ceta)).\
    filter( (df.Temp_Apa_C.S1 > 0) & (df.Temp_Apa_C.S2 > 0) & (df.Temp_Apa_C.S3 > 0) & (df.Temp_Apa_C.S4 > 0) & (df.Temp_Apa_C.S5 > 0) & (df.Temp_Apa_C.S6 > 0) ).\
    withColumn("temp_apa_c_max_bloc", udfBlocMaxNumaiPeBlocurileInTractiune(df.Stare_Ceta, df.Temp_Apa_C)).\
    withColumn("diff", udfDiffMaxMinNumaiPeBlocurileInTractiune(df.Stare_Ceta, df.Temp_Apa_C)).\
    sort(asc("diff"))

#     withColumn("belowThreshold", (udfDiffMaxMinBlocuri(df.Temp_Apa_R).lt(-40)).cast(IntegerType)).\
#     sort(asc("diff"))
    
# numar_total_de_hituri = table_filtered.count()
    #     filter(col("diff") > 5)
 
#     describe("diff").show()



# print table_filtered.count()
# 
# print table_filtered.where(table_filtered.diff>5)

table_filtered.registerTempTable("filtered")
# results = sqlContext.sql("SELECT DISTINCT Locomotiva, Count(*) OVER (PARTITION  BY Locomotiva) AS n from filtered")
# results = sqlContext.sql("WITH t1 as (SELECT   Locomotiva, temp_apa_r_max_bloc , COUNT(*) as NR_LOCO , FROM filtered GROUP BY  Locomotiva, temp_apa_r_max_bloc ) SELECT Locomotiva, temp_apa_r_max_bloc, NR_LOCO FROM t1")
# results = sqlContext.sql("WITH t1 as (SELECT   Locomotiva, temp_apa_r_max_bloc ,diff, COUNT(*) as NR_HITS_PER_BLOC, (SUM(case when diff>5 then 1 else 0 end)) AS DIFF_HITS, Data FROM filtered GROUP BY Locomotiva, temp_apa_r_max_bloc,diff, Data) SELECT Locomotiva, temp_apa_r_max_bloc, NR_HITS_PER_BLOC, DIFF_HITS,diff, SUM(NR_HITS_PER_BLOC) OVER (PARTITION BY Locomotiva) AS PERCENT, Data  FROM t1 GROUP BY Locomotiva, temp_apa_r_max_bloc, NR_HITS_PER_BLOC, DIFF_HITS, diff, Data ORDER BY Data ")
results = sqlContext.sql("WITH t1 as (SELECT   Locomotiva, temp_apa_c_max_bloc ,diff, COUNT(*) as NR_HITS_PER_BLOC, (SUM(case when diff>5 then 1 else 0 end)) AS DIFF_HITS, Data FROM filtered GROUP BY Locomotiva, temp_apa_c_max_bloc,diff, Data) SELECT Locomotiva, temp_apa_c_max_bloc, NR_HITS_PER_BLOC, DIFF_HITS,diff, SUM(NR_HITS_PER_BLOC) OVER (PARTITION BY Locomotiva) AS PERCENT, Data  FROM t1 GROUP BY Locomotiva, temp_apa_c_max_bloc, NR_HITS_PER_BLOC, DIFF_HITS, diff, Data ORDER BY Data ")


#results = sqlContext.sql("WITH t1 as (SELECT   Locomotiva, temp_apa_r_max_bloc ,diff,  (SUM(case when diff>5 then 1 else 0 end)) AS DIFF_HITS FROM filtered GROUP BY Locomotiva, temp_apa_r_max_bloc,diff) SELECT Locomotiva, temp_apa_r_max_bloc, DIFF_HITS,diff  FROM t1 GROUP BY Locomotiva, temp_apa_r_max_bloc, DIFF_HITS, diff  ")

results.registerTempTable("inainte_de_filtrare")
res = sqlContext.sql("Select * from inainte_de_filtrare where DIFF_HITS > 0").toPandas().to_csv('/home/mihai/ArhivaDateLema/somedata/temp/temp_apa_c_cu_blocuri_pe_tractiune.csv')

#res = sqlContext.sql("Select * from inainte_de_filtrare where DIFF_HITS > 0").show()

# results = sqlContext.sql("SELECT   Locomotiva, temp_apa_r_max_bloc , COUNT(*) as NR_LOCO,  (SUM(case when diff>5 then 1 else 0 end))*100/Count(Locomotiva) As Procent  FROM filtered GROUP BY  Locomotiva, temp_apa_r_max_bloc HAVING Procent >0 ORDER BY Locomotiva, Procent DESC ")



# results = sqlContext.sql("SELECT   Locomotiva, temp_apa_r_max_bloc , SUM(case when diff>5 then 1 else 0 end) As Nr_Hits  FROM filtered GROUP BY  Locomotiva, temp_apa_r_max_bloc HAVING Nr_Hits > 0 ORDER BY Locomotiva, Nr_Hits DESC ")
# nr_loco = sqlContext.sql("SELECT Locomotiva,  Count(Locomotiva) as NR_LOCO  from filtered group by Locomotiva ORDER BY NR_LOCO DESC")
# results.show()
# nr_loco.show(


# df.select(least(df.temp_apa_r.S1, df.temp_apa_r.S2).alias("min")).show(10)
     
def maxims(x):
    x_dict = x.asDict()   
    return max([ v for k,v in x_dict.iteritems() if k not in ('UM')])
        
def minims(x):
        
    x_dict = x.asDict()   
    return max([ v for k,v in x_dict.iteritems() if k not in ('UM')])      
    
         



        
    

 



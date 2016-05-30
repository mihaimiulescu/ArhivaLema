# def Wrapped_something_torun_Exception(l=4):
#     try:
#         something_torun_Exceptions(l)
#     except ValueError:
#         pass
# def something_torun_Exceptions(l = 4):
#     if (l<4) :
#         raise ValueError('este mai mic, introduceti unul mai mare')
#     else: print l
# def something_torun(l = 4):
#     if (l< 4):
#         print "mai mic ca 4"
#     else :
#         print l
# 
# def main():
#     
#     try:
#         map(Wrapped_something_torun_Exception , range(8))
#     except ValueError:
#         return None
# 
#    
#     
# if __name__ == "__main__":
#     main()


from pyspark.sql import SQLContext
from pyspark.sql.context import SQLContext
from pyspark.context import SparkContext
from pyspark.sql.functions import explode, least
from decimal import Decimal
from pyspark.sql.types import *

import json
from chardet.latin1prober import UDF
from types import NoneType
 
 
sc = SparkContext()      
sqlContext  = SQLContext(sc)
 
df = sqlContext.read.format("json").load("/home/mihai/ArhivaDateLema/somedata/temp/temp_home*")
df.select("stare_drv6", "stare_drv5").write.format("parquet").save("/home/mihai/ArhivaDateLema/somedata/temp/stare_drv_5_6.parquet")
df.unpersist()
df_pq = sqlContext.read.load("/home/mihai/ArhivaDateLema/somedata/temp/stare_drv_5_6.parquet")
df_pq.cache()
df_pq.show()
df.show()

# print df.count()




















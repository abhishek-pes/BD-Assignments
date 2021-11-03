import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import FloatType

sc = SparkContext.getOrCreate()
sql_context = SQLContext(sc)

path_to_city = sys.argv[1]
path_to_global = sys.argv[2]

df_city = sql_context.read.csv(path_to_city, header=True)
df_city = df_city.withColumn("AverageTemperature",df_city["AverageTemperature"].cast(FloatType()))
df_global = sql_context.read.csv(path_to_global,header=True)

df_grouped_temp = df_city.groupBy("dt","Country").max("AverageTemperature").withColumnRenamed("avg(AverageTemperature)","max_temp_on_date")
df3 = df_global.join(df_grouped_temp, df_global.dt == df_grouped_temp.dt ,how='inner')
df3 = df3.filter(df3["max(AverageTemperature)"] > df3["LandAverageTemperature"])

df3 = df3.groupBy("Country").count().collect()

if len(df3) > 0:
    result = sorted(list(map(lambda x : (x[0] , x[1]), df3)))
    for country,count in result:
        print("%s\t%s"%(country,count))
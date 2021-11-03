import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import FloatType

sc = SparkContext.getOrCreate()
sql_context = SQLContext(sc)

country = sys.argv[1]
path_df = sys.argv[2]

df = sql_context.read.csv(path_df, header=True)
df = df.withColumn("AverageTemperature",df["AverageTemperature"].cast(FloatType()))

df = df.filter(df.Country == country)
df_grouped = df.groupBy("City").avg("AverageTemperature").withColumnRenamed("avg(AverageTemperature)","total_avg")

df3 = df.join(df_grouped, df.City == df_grouped.City ,how='inner').drop(df_grouped.City)
df3 = df3.filter(df3.AverageTemperature > df3["total_avg"])
df3 = df3.groupBy("City").count().collect()

if len(df3) > 0:
    result = sorted(list(map(lambda x : (x[0] , x[1]), df3)))
    for city,count in result:
        print("%s\t%s"%(city,count))

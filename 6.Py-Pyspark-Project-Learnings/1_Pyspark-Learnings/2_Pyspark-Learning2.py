from pyspark.sql import SparkSession
import pyspark

spark = SparkSession.builder.config("spark.serializer","org.apache.spark.serializer.KryoSerializer").appName("Test").getOrCreate()

readSrc = spark.read.csv('/Users/rohan_shenoy/PycharmProjects/rohan-shenoy-prac-rep/6.Py-Pyspark-Project-Learnings/0_DataFile/Employee.csv',header=True,inferSchema=True).show()

readSrc.write.partitionBy("emp_dept").mode("overwrite").option("header","true").csv('/Users/rohan_shenoy/PycharmProjects/rohan-shenoy-prac-rep/6.Py-Pyspark-Project-Learnings/0.1_OutputFile')

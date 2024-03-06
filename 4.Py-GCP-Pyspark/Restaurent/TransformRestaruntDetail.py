from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, col

spark = SparkSession.builder.appName("Restaurant Transform").getOrCreate()

# Read the Parquet File from GCS

readCustDet = spark.read.format("parquet").load("gs://rs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/cust-det")\
.select(col("ID").alias("cust_id"),col("FIRST NAME").alias("cust_f_name"),col("LAST NAME").alias("cust_l_name"),col("company"))

readSaleDet = spark.read.format("parquet").load("gs://rs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/sales-det")\
.withColumnRenamed("Customer ID", "CUST_ID")\
.withColumnRenamed("Food ID", "FD_ID")

readFoodDet = spark.read.format("parquet").load("gs://rs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/food-det")


tfmCustFood = readCustDet.join(readSaleDet,readCustDet.cust_id == readSaleDet.CUST_ID, "inner")

finalDfDet = tfmCustFood.join()

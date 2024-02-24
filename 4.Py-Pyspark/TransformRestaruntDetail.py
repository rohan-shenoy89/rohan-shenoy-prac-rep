from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, col

spark = SparkSession.builder.appName("Restaurant Transform").getOrCreate()

# Read the Parquet File from GCS

readCustDet = spark.read.format("parquet").load("gs://rs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/cust-det")\
.withColumnRenamed("Customer ID", "CUST_ID")\
.withColumnRenamed("Food ID", "FD_ID")

readSaleDet = spark.read.format("parquet").load("gs://rs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/sales-det")

readFoodDet = spark.read.format("parquet").load("gs://rs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/food-det")


tfmCustFood = readCustDet.as("x").join(readSaleDet.as("y"), x.id == Customer ID )

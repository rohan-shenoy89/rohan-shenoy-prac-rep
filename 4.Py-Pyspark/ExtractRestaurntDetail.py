from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Restaurant").getOrCreate()


#Read Resturant Files

RestCust = "gs://rs-gcp-learning-bucket/restaurant-details/Restaurant - Customers.csv"
RestFood = "gs://rs-gcp-learning-bucket/restaurant-details/Restaurant - Foods.csv"
RestSales = "gs://rs-gcp-learning-bucket/restaurant-details/Restaurant - Week 1 Sales.csv"

readRestCust = spark.read.format("csv").option("header","True").option("inferSchema","True").load(RestCust)

readRestFood = spark.read.format("csv").option("header","True").option("inferSchema","True").load(RestFood)

readRestSales = spark.read.format("csv").option("header","True").option("inferSchema","True").load(RestSales)


#Check sample Data
readRestCust.show(10)
readRestFood.show(10)
readRestSales.show(10)

#Write data to cloud Storage
readRestCust.write.format("parquet").mode("overwrite").save("gs://rrs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/cust-det")

readRestFood.write.format("parquet").mode("overwrite").save("gs://rs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/cust-det")

readRestSales.write.format("parquet").mode("overwrite").save("gs://rs-gcp-learning-bucket/restaurant-details/write-restaurant-details-parquet/cust-det")


# Stop the SparkSession
spark.stop()

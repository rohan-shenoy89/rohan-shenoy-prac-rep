from pyspark.sql import SparkSession

#Create spark session

spark = SparkSession.builder.appName("Sample-GCP-Read").getOrCreate()

#Define file path
filePath = "rs-gcp-learning-bucket/employee-details"

# Read the CSV file into a DataFrame
df = spark.read.csv(filePath, header=True, inferSchema=True)

# Show the DataFrame schema
df.printSchema()

# Show the first few rows of the DataFrame
df.show()

# Stop the SparkSession
spark.stop()

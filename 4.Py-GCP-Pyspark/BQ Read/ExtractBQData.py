from pyspark.sql import SparkSession
from pyspark.sql import expr,col

#Create the Spark Session
spark = SparkSession.builder.appName("Read from BQ").getOrCreate()

#Read the BQ table
readBqTab = spark.read.format("bigquery").option("table","gcplearning-414410.EMPLOYEE_DETAILS.EMPLOYEE")\
    .load().cache()

#Check for sample data
readBqTab.show()

#Load the data to GCS
readBqTab.write.format("parquet").save("gs://rs-gcp-learning-bucket/employee-details/write-folder")

#Load Hig Salary data to BQ
readBqTabGrSal = readBqTab.selectExpr("cast(EMPLOYEE_ID as Integer) EMPLOYEE_ID","FIRST_NAME","LAST_NAME","JOB_ID","cast(SALARY as Integer) SALARY").filter("SALARY > 9000")

#Load the data back to BQ
(readBqTabGrSal.write.format("bigquery").option("temporaryGcsBucket","rs-gcp-learning-bucket").option("table","gcplearning-414410.EMPLOYEE_DETAILS.EMP_GR_SAL").mode("overwrite").save())

#Stop spark session
spark.stop()


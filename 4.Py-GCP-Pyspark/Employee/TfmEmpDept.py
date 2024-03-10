from pyspark.sql import SparkSession

#Create Spark Session

spark = SparkSession.builder.appName("Employee-Department-Details").getOrCreate

#Define File Path
empFilePath = "gs://rs-gcp-learning-bucket/employee-details"

DeptFilePath ="gs://rs-gcp-learning-bucket/employee-department"

#Reading the File from GCS

empReadDf = spark.read.format("csv").option("header","true").option("inferSchema","true").load(empFilePath)
#empReadDf = spark.read.csv(empFile/empFileName, header=True, inferSchema=True)

readEmpReqCols = empReadDf.selectExpr("cast(EMPLOYEE_ID as Integer) EMPLOYEE_ID",
                                      "concat(FIRST_NAME,' ', LAST_NAME) as EMPLOYEE_NM",
                                      "EMAIL as EMPLOYEE_EMAIL","cast(MANAGER_ID as Integer) MANAGER_ID",
                                      "cast(DEPARTMENT_ID as Integer) DEPARTMENT_ID")

deptReadDf = spark.read.format("csv").option("header","true").option("inferSchema","true").load(DeptFilePath).selectExpr("cast(DEPARTMENT_ID as Integer) as DEPARTMENT_ID", "DEPARTMENT_NAME")
#deptReadDf = spark.read.csv(DeptFile/DeptFileName, header=True, inferSchema=True)

#Join the Dataframes
tfmJoinEmpDept = readEmpReqCols.join(deptReadDf,readEmpReqCols.DEPARTMENT_ID == deptReadDf.DEPARTMENT_ID, "inner")\
.select("EMPLOYEE_ID","EMPLOYEE_NM","EMPLOYEE_EMAIL","MANAGER_ID","DEPARTMENT_NAME").filter("DEPARTMENT_NAME == 'IT Department'")


#Write to BQ Table
(tfmJoinEmpDept.write.format("bigquery").option("temporaryGcsBucket","rs-gcp-learning-bucket")\
 .option("table","gcplearning-414410.EMPLOYEE_DETAILS.EMP_IT_DEPT_DET").mode("append").save())

#Stop spark session
spark.stop()

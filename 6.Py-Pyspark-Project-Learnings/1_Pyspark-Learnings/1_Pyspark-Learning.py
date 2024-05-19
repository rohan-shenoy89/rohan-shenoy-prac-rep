from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Employee").getOrCreate()
empDf = spark.read.format("csv").option("header","true").option("infereSchema","true").load('/Users/rohan_shenoy/PycharmProjects/rohan-shenoy-prac-rep/6.Py-Pyspark-Project-Learnings/0_DataFile/Employee.csv')



#Another way of writing the read

empDf2 = spark.read.csv('/Users/rohan_shenoy/PycharmProjects/rohan-shenoy-prac-rep/6.Py-Pyspark-Project-Learnings/0_DataFile/Employee.csv',header=True,inferSchema=True)

readColumns = empDf2.select("emp_id","emp_nm","emp_loc")


# Adding columns in dataframes

addColDf = readColumns.withColumn('New_Emp_Id',readColumns['emp_id']+2)
addColDf = addColDf.drop('New_Emp_Id')

## Drop null values
addColDf2 = addColDf.na.drop(how="any",subset="emp_loc")

addColDf2.show()

## Fill the null values

fillMissVal = addColDf.na.fill('Missing Value','emp_nm')
fillMissVal.show()

## Filter operation
fillMissVal.filter((fillMissVal['emp_loc'] == 'Mumbai') | (fillMissVal['emp_loc'] == 'Sangli')).select("emp_nm","emp_loc").show()

##Aggregation
from pyspark.sql import SparkSession
from pyspark.sql import functions

spark = SparkSession.builder.appName("Practice2").getOrCreate()
sc = spark.sparkContext
readSrcDf = spark.read.csv('/Users/rohan_shenoy/PycharmProjects/rohan-shenoy-prac-rep/6.Py-Pyspark-Project-Learnings/0_DataFile/Employee.csv',header=True,inferSchema=True)

aggReadDf = readSrcDf.select("emp_dept","emp_sal").groupBy("emp_dept").sum("emp_sal")
maxEmpSalDf = readSrcDf.select("emp_dept","emp_sal").groupBy("emp_dept").max("emp_sal")
countEmpDept = readSrcDf.select("emp_dept").groupBy("emp_dept").count()
dirAggFun = readSrcDf.agg({"emp_sal":"sum"})

#aggReadDf.show(10)
#maxEmpSalDf.show(10)
#countEmpDept.show(10)
#dirAggFun.show(10)

readSrcDf.select("emp_nm").orderBy("emp_nm").isEmpty()


readSrcDf.repartition(2)





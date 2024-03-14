--> DATAPROC

**Create Cluster** - gcloud dataproc clusters create rs-gcp-learning-cluster --region asia-south1 --zone asia-south1-a --single-node --master-machine-type n2-standard-4 --master-boot-disk-size 500 --image-version 2.1-debian11 --project gcplearning-414410

**Run job via Shell** - gcloud dataproc jobs submit pyspark --cluster rs-gcp-learning-cluster gs://rs-gcp-learning-spark-repo/ExtractRestaurntDetail.py --region asia-south1 --project gcplearning-414410

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--> CLOUD STORAGE

**Create Bucket** - gsutil mb gs://rs-gcp-learning-temp

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--> BIG QUERY COMMANDS

**Help Option** - bq help

**List dataset** - bq ls

**View Public Dataset** - bq ls publicdata:samples

**Make new Dataset** - bq mk rohanlearn_dataset

**Delete Dataset** - bq rm rohanlearn_dataset

**Get information of Dataset** - bq show publicdata:samples.shakespeare

**Run SQL** - bq query "SELECT count(distinct corpus) FROM `bigquery-public-data.samples.shakespeare` LIMIT 1000"

**Show detais about Dataset** - bq show --format=prettyjson gcpBqLearning

**Update the dataset persmissions** - bq update --source <json file> <dataset_name>

**Run the command on Query tab for table info** - select * from gcpBqLearning.__TABLES_SUMMARY__
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

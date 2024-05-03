--> DATAPROC

**Create Cluster** - gcloud dataproc clusters create rs-gcp-learning-cluster --region asia-south1 --zone asia-south1-a --single-node --master-machine-type n2-standard-4 --master-boot-disk-size 500 --image-version 2.1-debian11 --project gcplearning-414410

**Create Preemptible Cluster** - gcloud dataproc clusters create rs-gcp-learning-prem-cluster \
--num-secondary-workers 1 --region asia-south1 --zone asia-south1-a \
--master-machine-type n2-standard-4 --master-boot-disk-size 30 \
--num-workers 2 --worker-machine-type n2-standard-2 \
--worker-boot-disk-size 30

**Initilization action to add software** - gcloud dataproc clusters create <cluster name> --initialization-actions gs://$MY_BUCKET/hbase/hbase.sh --num-master 3 --num-workers 2

**Run job via Shell** - gcloud dataproc jobs submit pyspark --cluster rs-gcp-learning-cluster gs://rs-gcp-learning-spark-repo/ExtractRestaurntDetail.py --region asia-south1 --project gcplearning-414410

**Create a cluster with primary-worker shuffle** - gcloud dataproc clusters create cluster-name \
    --region=region \
    --properties=dataproc:efm.spark.shuffle=primary-worker \
    --properties=dataproc:efm.mapreduce.shuffle=hcfs \
    --worker-machine-type=n1-highmem-8 \
    --num-workers=25 \
    --num-worker-local-ssds=2 \
    --secondary-worker-type=preemptible \
    --secondary-worker-boot-disk-size=500GB \
    --num-secondary-workers=25

**Disable autoscaling** - gcloud dataproc clusters update \
    --cluster=cluster-name \
    --region=region \
    --disable-autoscaling

**Scale the primary group** - gcloud dataproc clusters update \
    --cluster=cluster-name \
    --region=region \
    --num-workers=num-primary-workers \
    --graceful-decommission-timeout=graceful-decommission-timeout

**Re-enable autoscaling** - gcloud dataproc clusters update \
    --cluster=cluster-name \
    --region=region \
    --autoscaling-policy=autoscaling-policy
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

**Run SQL** - bq query "SELECT * FROM bigquery_public_data.google_trends.top_terms LIMIT 1000"

**Show detais about Dataset** - bq show --format=prettyjson gcpBqLearning

**Update the dataset persmissions** - bq update --source <json file> <dataset_name>

**Run the command on Query tab for table info** - select * from gcpBqLearning.__TABLES_SUMMARY__

**Create partitioned data via shell** - bq mk --table --schema OrderId:STRING,OrderDate:DATE,Quantity:INTEGER --time_partitioning_field OrderDate gcplearning-414410.restaurant_dataset.order_data
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--> Cloud Composer

**update pypi package** - gcloud composer environments update rs-gcp-learning-composer2 \
--update-pypi-packages-from-file /home/cloud_user/requirements.txt \
--location east-south-1
--async

**Define Airflow variables** - gcloud composer environments run rs-gcp-learning-composer2 \
--location east-south-1
--set <variable_name> rs-gcp-learning

**set locations for GCS operations** - gcloud composer environments run rs-gcp-learning-composer2 \
--location east-south-1 variables -- \
--set <source_name> <bucket_name>

gcloud composer environments run rs-gcp-learning-composer2 \
--location east-south-1 variables -- \
--set <destination_name> <bucket_name>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--> Cloud SQL

**Get details about SQL** - gcloud sql instances patch --help

**Stop instance** - gcloud sql instances patch rs-gcp-learning-sql --activation-policy NEVER

**Start instance** - gcloud sql instances patch rs-gcp-learning-sql --activation-policy ALWAYS

**Restart the instance** - gcloud sql instances restart rs-gcp-learning-sql

**Delete Instance** - gcloud sql instances delete rs-gcp-learning-sql

**Connect to SQL - root user** - gcloud sql connect rs-gcp-learning-sql1 --user=root

**Connect to SQL - root developer** - gcloud sql connect rs-gcp-learning-sql1 --user=developer

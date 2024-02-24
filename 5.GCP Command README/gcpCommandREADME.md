--> DATAPROC

**Create Cluster** - gcloud dataproc clusters create rs-gcp-learning-cluster --region asia-south1 --zone asia-south1-a --single-node --master-machine-type n2-standard-4 --master-boot-disk-size 500 --image-version 2.1-debian11 --project gcplearning-414410

**Run job via Shell** - gcloud dataproc jobs submit pyspark --cluster rs-gcp-learning-cluster gs://rs-gcp-learning-spark-repo/ExtractRestaurntDetail.py --region asia-south1 --project gcplearning-414410

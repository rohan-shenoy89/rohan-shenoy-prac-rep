from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.dates import days_ago
from datetime import datetime

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define DAG
dag = DAG(
    'gcp_composer_sample_dag',
    default_args=default_args,
    description='A sample DAG interacting with GCP services',
    schedule_interval='@once',
    start_date=datetime(2024, 3, 17),
    catchup=False
)

# Define task to load data from GCS to BigQuery
gcs_to_bigquery_task = GCSToBigQueryOperator(
    task_id='load_data_to_bigquery',
    bucket='rs-gcp-learning-bucket',
    source_objects=['Employee_Department.csv'],
    destination_project_dataset_table='gcplearning-414410.gcpBqLearning.sample_depart_det',
    schema_fields=[{'DEPARTMENT_ID': 'DEPARTMENT_ID', 'type': 'INTEGER'}, {'DEPARTMENT_NAME': 'DEPARTMENT_NAME', 'type': 'STRING'}],
    skip_leading_rows=1,
    write_disposition='WRITE_TRUNCATE',
    trigger_rule='one_failed',
    dag=dag
)

# Define SQL query to execute in BigQuery
sql_query = """
SELECT * FROM gcplearning-414410.gcpBqLearning.sample_depart_det LIMIT 10
"""

# Define task to execute SQL query in BigQuery
bigquery_execute_query_task = BigQueryExecuteQueryOperator(
    task_id='execute_bigquery_query',
    sql=sql_query,
    use_legacy_sql=False,
    dag=dag
)

# Define task dependencies
gcs_to_bigquery_task >> bigquery_execute_query_task

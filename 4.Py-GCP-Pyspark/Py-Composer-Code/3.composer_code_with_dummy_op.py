from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators import dummy_operator
from datetime import datetime

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the Python function to print "Hello, World!"
def print_hello():
    print("Hello, World!")

# Define the DAG
with DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple DAG to print Hello, World!',
    schedule_interval=None,  # Run once
    start_date=datetime(2023, 3, 17),
    catchup=False,
) as dag:

    # Define the PythonOperator to execute the print_hello function
    hello_task = PythonOperator(
        task_id='print_hello_task',
        python_callable=print_hello
    )

    end = dummy_operator,DummyOperator(
        task_id='dummy'
    )

    # Set task dependencies
    hello_task >> end

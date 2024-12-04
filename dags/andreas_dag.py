from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from google.cloud import bigquery
import pandas as pd
import os
from airflow.utils.dates import days_ago

# Set environment variable for Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/opt/airflow/dags/SA.json"

# BigQuery configuration
project_id = "sage-outrider-418915"
destination_table = "dwh_retail_transactions.raw_retail"  # e.g., dataset.table_name
sql_query = "SELECT * FROM retail_transactions;"  # Modify with your table/query

def extract_data():
    """Extract data from PostgreSQL and return as DataFrame using PostgresHook"""
    try:
        # Use PostgresHook to connect to PostgreSQL using the connection ID (conn_id)
        pg_hook = PostgresHook(postgres_conn_id='postgres_local')
        print("Connecting to PostgreSQL using Airflow connection...")

        # Running the SQL query
        print("Executing query...")
        df = pg_hook.get_pandas_df(sql_query)  # This returns the query result as a DataFrame

        print("Data successfully extracted from PostgreSQL.")
        return df
    except Exception as e:
        print(f"An error occurred during extraction: {e}")
        raise

def load_data_to_bigquery(**kwargs):
    """Load data to BigQuery"""
    try:
        # Get the DataFrame from XCom
        df = kwargs['ti'].xcom_pull(task_ids='extract_data')
        
        if df is not None:
            print("Writing data to BigQuery...")
            df.to_gbq(destination_table, project_id=project_id, if_exists="replace")
            print("Data successfully written to BigQuery!")
        else:
            print("No data to load to BigQuery.")
    except Exception as e:
        print(f"An error occurred during loading to BigQuery: {e}")
        raise

# Define the DAG
dag = DAG(
    'extract_load_data_dag',
    description='Extract data from PostgreSQL and load into BigQuery By Andreas Silaen - Test Lion Parcel - Data Engineer',
    schedule_interval="@hourly",  # Run every hour
    start_date=days_ago(1),
    catchup=False,
)

# Define the tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data_to_bigquery',
    python_callable=load_data_to_bigquery,
    provide_context=True,
    dag=dag,
)

# Task dependencies
extract_task >> load_task

import pandas as pd
import os
import psycopg2
from sqlalchemy import create_engine

# SERVICE ACCOUNT
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/AndreasSilaen/Python File check/Belajar/Task_1/SA.json"


# PostgreSQL configuration
pg_config = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "admin",
    "port": "5432",  # Default PostgreSQL port
}

# BigQuery configuration
project_id = "sage-outrider-418915"
destination_table = "dwh_retail_transactions.raw_retail"  # e.g., dataset.table_name

# Query to fetch data from PostgreSQL
sql_query = "SELECT * FROM retail_transactions"  # Modify with your table/query

try:
    # Connect to PostgreSQL
    engine = create_engine(
        f"postgresql+psycopg2://{pg_config['user']}:{pg_config['password']}@{pg_config['host']}:{pg_config['port']}/{pg_config['database']}"
    )
    print("Connecting to PostgreSQL...")
    with engine.connect() as connection:
        # Read data into a Pandas DataFrame
        print("Reading data from PostgreSQL...")
        df = pd.read_sql(sql_query, connection)

    # Write DataFrame to BigQuery
    print("Writing data to BigQuery...")
    df.to_gbq(destination_table, project_id=project_id, if_exists="replace")
    print("Data successfully written to BigQuery!")

except Exception as e:
    print("An error occurred:", e)

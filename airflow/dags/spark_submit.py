from datetime import datetime 
from airflow import DAG 
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 

with DAG(dag_id='spark_submit_operator_example', start_date=datetime(2025, 3, 9)) as dag: 
    submit_spark_job = SparkSubmitOperator(
        task_id='submit_spark_job',
        application='/opt/airflow/jobs/test_pyspark_job.py',  # Replace with the path to your spark_job.py
        conn_id='spark_default',  # Connection to Spark cluster (adjust if needed)
        executor_cores=1,
        executor_memory='1g',
        num_executors=2,
        driver_memory='1g',
        verbose=True,
        name='SparkTest'
    ) 

    submit_spark_job


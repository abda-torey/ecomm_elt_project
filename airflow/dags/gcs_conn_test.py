from datetime import datetime 
from airflow import DAG 
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 3, 9),
    'retries': 1,
}

with DAG(
    'spark_gcs_job',
    default_args=default_args,
    schedule_interval=None,  # Set to your desired schedule
) as dag:

    spark_task = SparkSubmitOperator(
        task_id='submit_spark_gcs_job',
        conn_id='spark_default',  # Ensure this connection is set up in Airflow
        application='/opt/airflow/jobs/gcc_test_job.py',  # Path to your PySpark script
        conf={
            'spark.master': 'spark://spark:7077',
            'spark.executor.memory': '2g',  # Reduce per-executor memory
            'spark.executor.cores': '1',     # Reduce cores per executor
            'spark.executor.instances': '2',
            'spark.hadoop.fs.gs.impl': 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem',
            'spark.hadoop.fs.gs.auth.service.account.enable': 'true',
            'spark.hadoop.fs.gs.auth.service.account.json.keyfile': '/opt/airflow/keys/first-key.json',
        },
        jars='/opt/airflow/jars/gcs-connector-hadoop3-2.2.0.jar',
        verbose=True,
    )

    spark_task

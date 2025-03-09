from pyspark.sql import SparkSession
from pyspark.sql import functions as F
# Initialize Spark session
spark = SparkSession.builder \
    .appName("Spark to BigQuery Test") \
    .getOrCreate()

# Example: Read a CSV file from GCS
df = spark.read.csv('gs://final_ecom_taxi-data-447320/products.csv', header=True)

# Rename columns to valid BigQuery column names
df = df.withColumnRenamed("1", "column_1") \
       .withColumnRenamed("286.75", "column_286_75") \
       .withColumnRenamed("789", "column_789") \
       .withColumnRenamed("syndicate extensible initiatives", "syndicate_initiatives") \
       .withColumnRenamed("resource", "resource_column")

# Cast numeric columns to the correct types (e.g., float)
df = df.withColumn("column_286_75", F.col("column_286_75").cast("float")) \
       .withColumn("column_789", F.col("column_789").cast("float"))

# Verify the new schema
df.printSchema()
# Write DataFrame to BigQuery

df.write \
  .format("bigquery") \
  .option("writeMethod", "direct") \
  .mode("overwrite") \
  .save("taxi-data-447320.ecom_project_data.bigquerry_test")

spark.stop()
 
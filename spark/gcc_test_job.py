from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("GCSConnectorTest") \
    .getOrCreate()

# Set the GCS bucket URL (replace with your GCS bucket)
gcs_bucket_path = "gs://final_ecom_taxi-data-447320/products.csv"

# Read data from GCS bucket (assuming it's a CSV file)
df = spark.read.csv(gcs_bucket_path, header=True)

# Show some data
df.show()

# Stop the Spark session
spark.stop()

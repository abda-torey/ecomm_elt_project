from pyspark.sql import SparkSession

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("SparkTest") \
    .getOrCreate()

# Create a sample DataFrame
data = [("John", 28), ("Jane", 25), ("Doe", 35)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Perform a transformation (e.g., filtering)
df_filtered = df.filter(df.Age > 30)

# Show the filtered DataFrame
df_filtered.show()

# Stop the Spark session
spark.stop()

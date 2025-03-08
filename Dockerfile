# Use an official Apache Spark image as the base
FROM bitnami/spark:3.3.1

# Set environment variables
ENV GOOGLE_APPLICATION_CREDENTIALS=/opt/spark/gcs-key.json

# Install required Python libraries
RUN pip install google-cloud-storage google-cloud-bigquery

# Copy the GCS service account key into the container
COPY gcs-key.json /opt/spark/gcs-key.json

# Set the working directory
WORKDIR /opt/spark

# Expose Spark UI port
EXPOSE 4040

# Start Spark master and worker
CMD ["spark-class", "org.apache.spark.deploy.master.Master"]

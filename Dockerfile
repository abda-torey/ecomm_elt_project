FROM apache/airflow:2.10.4-python3.12

USER root
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64



USER airflow

RUN pip install apache-airflow apache-airflow-providers-apache-spark pyspark
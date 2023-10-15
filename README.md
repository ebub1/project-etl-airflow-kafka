# project-etl-airflow-kafka
Overwiev
n this final assignment module of ETL and Data Pipelines with Shell, Airflow and Kafka, you will apply your newly gained knowledge to explore two very exciting hands-on labs. “Creating ETL Data Pipelines using Apache Airflow” and “Creating Streaming Data Pipelines using Kafka”. You will explore...
In this project I perform ETL, create a pipeline and upload the data into a database. And use both Airflow and Kafka.

Scenario
I have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with different IT setup that use different file formats.  In the first module job is to collect data available in different formats and, consolidate it into a single file.  
As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id and timestamp are streamed to Kafka. In the second module job is to create a data pipeline that collects the streaming data and loads it into a database.

Module 1: ETL & Apeche Airflow
  Need to create DAG that does:
    - Extract data from a csv file
    - Extract data from a tsv file
    - Extract data from a fixed width file
    - Transform the data
    - Load the transformed data into the staging area
  
  1. Defint



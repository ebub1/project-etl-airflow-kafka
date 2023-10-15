# project-etl-airflow-kafka
<img width="649" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/edfcef6e-b258-4608-a8da-7093534c34b4">

Overview.

Final project of [ETL and Data Pipelines with Shell, Airflow and Kafka](https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka/home/info).“Creating ETL Data Pipelines using Apache Airflow” and “Creating Streaming Data Pipelines using Kafka”.

Scenario.

The project  aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with different IT setup that use different file formats.  In the first module job is to collect data available in different formats and, consolidate it into a single file.  
As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id and timestamp are streamed to Kafka. In the second module job is to create a data pipeline that collects the streaming data and loads it into a database.

**Module 1: Creating ETL Data Pipelines using Apache Airflow.**

  Need to create DAG that does:
    - Extract data from a csv file
    - Extract data from a tsv file
    - Extract data from a fixed width file
    - Transform the data
    - Load the transformed data into the staging area
  
  1. Define DAG args and the DAG:
   
<img width="551" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/386ea569-6a46-4b1e-a3b5-fc7773d8e5be">

  3. Create tasks for unziping and extracting data:

<img width="660" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/e0b87780-e3fd-4fe7-b920-30f475365e14">

  3.Create tasks to consolidate and transform extracted data:
  
<img width="558" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/e47d384b-7284-4b7d-bf71-9689c2568b57">

  4. Define the task pipeline:
     
<img width="1085" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/8026ef1c-9a9a-4e02-b289-2f495d2b49bb">

  6. Submit DAG and check:
     
<img width="1072" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/23a6c44d-a1ef-4771-a8f9-5e5968b04c8f">

  8. Unpause DAG and monitor:
     
<img width="1861" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/c394bc29-88d6-4800-8fe3-8df68bd57dd1">









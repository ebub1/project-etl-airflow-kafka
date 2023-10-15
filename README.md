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
     
<img width="1071" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/1d7f3cc3-2b6c-4858-a37f-c2fae4204069">

  8. Unpause DAG and monitor:
     
<img width="1861" alt="image" src="https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/b345a0f4-3744-4d14-a466-8e0561429fb2">


__Module 2: Creating Streaming Data Pipelines using Kafka__

  1. Start Zookeper:
![2 1_start_zookeeper](https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/c16090c0-f41b-4ae3-93d5-a06afa5a2a97)

  2. Start Kafka server:
![2 2_start_kafka_server](https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/4533d7ea-31c5-43fc-aa95-fecbfd425102)

  3. Create a topic named toll:
![2 3_create_toll_topic](https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/fb5e2363-8d8f-4b85-8bd9-aba840851234)

  4. Data generates bby toll_traffic_generator:
![2 6_simulator_output](https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/d76702f9-2b12-4421-9a1f-a85f6512e374)

  5. Data streams by streaming_data_reader.py:
![2 8_data_reader_output](https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/70e0430c-c49f-485d-8105-e66d9c3eb0c2)

  6. Health check of the streaming data pipeline:
![2 9_output_rows](https://github.com/ebub1/project-etl-airflow-kafka/assets/121383182/f11c15a4-5aab-44c9-9209-1bd0d62e54bb)









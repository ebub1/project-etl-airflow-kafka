# import the libraries

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments

default_args = {
    'owner': 'Eugene B',
    'start_date': days_ago(0),
    'email': ['eugene-b@mail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=0.5),
}

# defininig the DAG

dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# defininig the tasks

# task for unzip data

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command="""tar -xvzf /home/project/airflow/dags/finalassignment/tolldata.tgz""",
    dag=dag
)

# task for extracting data from csv file

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="""cut -f 1,2,3,4 -d "," 
    /home/project/airflow/dags/finalassignment/vehicle-data.csv 
    > /home/project/airflow/dags/finalassignment/csv_data.csv """,
    dag=dag
)

# task for extracting data from tsv file

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="""cut -f 5,6,7 
    /home/project/airflow/dags/finalassignment/tollplaza-data.tsv 
    > /home/project/airflow/dags/finalassignment/tsv_data.csv """,
    dag=dag
)

#task for extracting data from fixed width file

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="""cut -c59-62,63-68 
    /home/project/airflow/dags/finalassignment/payment-data.txt
     > /home/project/airflow/dags/finalassignment/fixed_width_data.csv""",
    dag=dag
)

#task for consolidating extracted data from privious tasks

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="""paste csv_data.csv tsv_data.csv fixed_width_data.csv 
    > /home/project/airflow/dags/finalassignment/extracted_data.csv  """,
    dag=dag
)
# transform

transform_data = BashOperator(
    task_id='transform_data',
    bash_command="""awk 'BEGIN {FS=OFS=","} { $4 = toupper($4) } 1' 
    /home/project/airflow/dags/finalassignment/extracted_data.csv
    > /home/project/airflow/dags/finalassignment/transformed_data.csv""",
    dag=dag
)

# task pipeline

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data


tar -xvzf /home/project/airflow/dags/finalassignment/tolldata.tgz
cut -f 1,2,3,4 -d "," /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv 
cut -f 5,6,7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv
cut -c 59-62, 63-68 /home/project/airflow/dags/finalassignment/payment-data.txt > sed -i 's/ \+/,/g' /home/project/airflow/dags/finalassignment/fixed_width_data.csv
tr -f 3 d"," "[a-z]" "[A-Z]" < /home/project/airflow/dags/finalassignment/extracted_data.csv > /home/project/airflow/dags/transformed_data.csv
awk 'BEGIN {FS=OFS=","} { $3 = toupper($3) } 1' /home/project/airflow/dags/finalassignment/extracted_data.csv > /home/project/airflow/dags/finalassignment/transformed_data.csv
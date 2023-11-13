from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta

# Define Task for Data Ingestion and data serving
# Running bash Script for BQ Load and Script apache Beam SDK
sources = [
    {"num": 1, "task_ingest_name": "table_data1.sh", "path_ingestion": "test1/path/"},
    {"num": 1, "task_ingest_name": "table_data2.sh", "path_ingestion": "test1/path/"}, 
    {"num": 1, "task_ingest_name": "table_data3.sh", "path_ingestion": "test1/path/"},
    {"num": 2, "task_ingest_name": "table_data4.sh", "path_ingestion": "test2/path/", 
     "task_serving_name" : "serving_data1.sh", "path_serving" : "test1/path/"},
    {"num": 2, "task_ingest_name": "table_data5.sh", "path_ingestion": "test2/path/", 
     "task_serving_name" : "serving_data2.sh", "path_serving" : "test1/path/"},
    {"num": 2, "task_ingest_name": "table_data6.sh", "path_ingestion": "test2/path/", 
     "task_serving_name" : "serving_data3.sh", "path_serving" : "test1/path/"},
    ]

# define the DAG
with DAG(
    "dynamic_Task",
    default_args={
        "owner": "me",
        "depends_on_past": False,
        "email_on_failure": False,
        "email_on_retry": False,
    },
    description="test_dag test description.",
    start_date=datetime(2022, 2, 1),
    schedule_interval=None,
    max_active_runs=1,
) as dag:

    data_ingestion_start = DummyOperator(task_id="data_ingestion_start")

    with TaskGroup(group_id="group_data_ingestion") as group_data_ingestion:
        for source in sources:
            if source['num'] == 1:
                ingest_table = BashOperator(
                    task_id=f"ingestion_table_{source['task_ingest_name']}",
                    bash_command="{}/{} ".format({source['path_ingestion']}, {source['task_ingest_name']}),
                    dag=dag,
                )
            elif source['num'] == 2:
                ingest_table = BashOperator(
                    task_id=f"ingestion_table_{source['task_ingest_name']}",
                    bash_command="{}/{} ".format({source['path_ingestion']}, {source['task_ingest_name']}),
                    dag=dag,
                )
                serving_table = BashOperator(
                    task_id=f"serving_table_{source['task_ingest_name']}",
                    bash_command="{}/{} ".format({source['path_serving']}, {source['task_serving_name']}),
                    dag=dag,
                )
                ingest_table >> serving_table

    data_ingestion_end = DummyOperator(task_id="data_ingestion_end")

    data_ingestion_start >> group_data_ingestion >> data_ingestion_end

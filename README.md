Dynamically Generate Task Using Dictionary Element in Airflow

Suppose for example we want to execute multiple script in same manner in parallely,
Instead to repeatly defining 

```
task_name = BashOperator(
            task_id='task_name',
            bash_command="{}/{} ".format()
        )
```

We able to just create a dict which defining how many task we want to execute.

```
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
```

and then Loop for each dict element, to dynamically generate the Task.

```
for source in sources:
    ingest_table = BashOperator(
        task_id=f"ingestion_table_{source['task_ingest_name']}",
        bash_command="{}/{} ".format({source['path_ingestion']}, {source['task_ingest_name']}),
        dag=dag,
    )
```

Illustration for the result

![Sample Image](https://raw.githubusercontent.com/muhk01/airflow_dynamic_task/main/img/dynamic_task.PNG)


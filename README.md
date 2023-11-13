Dynamically Generate Task Using Dictionary Element in Airflow

Suppose for example we want to execute some script with only one dependency, or more than one, in parallely.

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

Illustration for the result

![Sample Image](https://raw.githubusercontent.com/muhk01/airflow_dynamic_task/main/img/dynamic_task.PNG)


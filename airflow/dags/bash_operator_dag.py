from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "sawradip",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="basic_bash_dag_v2",
    default_args=default_args,
    description="Our basic Bash DAG",
    start_date=datetime(2024, 9, 16, 11, ),
    schedule_interval="@daily",
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo Hi, I am first Task!"
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo Hi, I am first Task!"
    )

    # task3 = BashOperator(
    #     task_id="first_task",
    #     bash_command="echo Hi, I am first Task!"
    # )

    task1 >> task2  #, task3]
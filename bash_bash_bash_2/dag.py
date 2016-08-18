from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 1, 1, 1, 0),
    'email': ['xuanji@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
    'concurrency': 1,
}

dag = DAG('bash_bash_bash_2', default_args=default_args, schedule_interval=timedelta(seconds=10))

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)


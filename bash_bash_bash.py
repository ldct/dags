# Record datadog metrics into a DB for easier SLA reporting

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
}

dag = DAG('bash_bash_bash', default_args=default_args, schedule_interval=timedelta(seconds=10))

# t1, t2 and t3 are examples of tasks created by instatiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 1',
    retries=3,
    dag=dag
)

templated_command = """
{% for i in range(5) %}
echo "{{ ds }}"
echo "{{ macros.ds_add(ds, 7)}}"
echo "{{ params.my_param }}"
{% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag
)

t2.set_upstream(t1)
t3.set_upstream(t1)

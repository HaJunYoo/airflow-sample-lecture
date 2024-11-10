from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

# Default arguments 설정
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 27, hour=0, minute=00),
    'email': ['hajuny129@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
}

# DAG 정의
dag = DAG(
    "bash_operation_v2",  # DAG name
    schedule="0 9 * * *", # 매일 오전 9시에 실행
    tags=['test'],
    catchup=False,
    default_args=default_args
)

# Start task
start = DummyOperator(
    task_id="start",
    dag=dag
)

# First bash task
t1 = BashOperator(
    task_id='ls1',
    bash_command='ls /tmp/downloaded',
    retries=3,
    dag=dag
)

# Second bash task
t2 = BashOperator(
    task_id='ls2',
    bash_command='ls /tmp/downloaded',
    dag=dag
)

# End task
end = DummyOperator(
    task_id='end',
    dag=dag
)

# Task 의존성 설정
start >> t1 >> t2 >> end
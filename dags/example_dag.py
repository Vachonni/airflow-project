from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def hello():
    print("Hello from Airflow DAG")


def generate_fail():
    raise ValueError("Intentional failure for testing")


def default_args():
    return {
        'owner': 'airflow',
        'depends_on_past': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    }

with DAG(
    dag_id='example_dag',
    default_args=default_args(),
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['example'],
) as dag:
    t1 = PythonOperator(
        task_id='hello',
        python_callable=hello,
    )

    t2 = PythonOperator(
        task_id='fail',
        python_callable=generate_fail,
        trigger_rule='all_done'
    )

    t1 >> t2

from airflow import DAG
# from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id="prepro_to_transac_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract = DockerOperator(
        task_id="extract_data",
        image="prepro:dev",
        environment={"DATABASES_URL": "{{ var.value.DATABASES_URL }}"},
        command="--step extract --file_path /blob/dev/raw/2025/8/N_Revolut.csv",
        docker_url="unix://var/run/docker.sock",
        auto_remove=True,
    )

    clean = DockerOperator(
        task_id="clean_data",
        image="prepro:dev",
        command="--step clean",
        docker_url="unix://var/run/docker.sock",
        auto_remove=True,
    )

    normalize = DockerOperator(
        task_id="normalize_data",
        image="prepro:dev",
        command="--step normalize",
        docker_url="unix://var/run/docker.sock",
        auto_remove=True,
    )

    extract >> clean >> normalize

    # trigger_preprocessing = TriggerDagRunOperator(
    #     task_id="run_preprocessing",
    #     trigger_dag_id="preprocessing_dag",  # nom du DAG cible
    # )

    # train = DockerOperator(
    #     task_id="train_model",
    #     image="training:latest",
    #     command="python train.py",
    #     docker_url="unix://var/run/docker.sock",
    #     auto_remove=True,
    # )

    # evaluate = DockerOperator(
    #     task_id="evaluate_model",
    #     image="evaluation:latest",
    #     command="python evaluate.py",
    #     docker_url="unix://var/run/docker.sock",
    #     auto_remove=True,
    # )

    # trigger_preprocessing >> train >> evaluate
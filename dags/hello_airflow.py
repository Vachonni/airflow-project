from datetime import datetime
import logging
from airflow import DAG
from airflow.decorators import task

log = logging.getLogger(__name__)

with DAG(
    dag_id="hello_airflow",
    schedule=None,  # Manual trigger only
    start_date=datetime(2025, 8, 21),
    catchup=False,
    tags=["example"],
    doc_md="""
    ### Hello Airflow
    Simple TaskFlow DAG showing best-practice:
    - Use return value (XCom) from first task fed as argument to second
    - Use structured logging (logger.info) instead of bare print
    """,
) as dag:

    @task
    def say_hello() -> str:
        """Return a greeting (stored in XCom)."""
        log.info("Generating greeting")
        return "Hello from Airflow"

    @task
    def print_msg(msg: str) -> None:
        """Log the provided message."""
        log.info("Message received: %s", msg)

    # TaskFlow dependency (implicit via argument passing)
    print_msg(say_hello())

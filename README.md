Airflow Docker Compose scaffold

This project provides a minimal Apache Airflow setup using Docker Compose and the official apache/airflow image.

Files created:
- .env - environment variables used by docker-compose
- docker-compose.yaml - compose file defining Postgres, Redis, and Airflow services
- dags/example_dag.py - a simple example DAG
- dags/ - directory for DAGs
- plugins/ - directory for plugins
- logs/ - directory mounted for Airflow logs
- data/postgres - Postgres data volume

Quick start (macOS / zsh):

1. Export UID/GID (optional if you keep defaults in .env):

```bash
export AIRFLOW_UID=$(id -u)
export AIRFLOW_GID=$(id -g)
```

2. Initialize the database (create the airflow DB and user):

```bash
docker compose up airflow-webserver -d
# in another terminal, run the init container if needed
docker compose run --rm airflow-webserver airflow db init
```

3. Create an admin user:

```bash
docker compose run --rm airflow-webserver airflow users create \
  --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
```

4. Start the full stack:

```bash
docker compose up -d
```

5. Open the web UI at http://localhost:8080 (username/password: admin/admin)

Notes:
- This is a minimal scaffold. For production or more advanced development, consult the official Apache Airflow Docker documentation: https://airflow.apache.org/docs/
- Consider using the official Airflow docker-compose example repository for a more complete setup with scheduler, worker, flower, and init containers.

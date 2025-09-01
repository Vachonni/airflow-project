DOCKER_COMPOSE = docker compose


.PHONY: help init up down reset

	@echo "Root Makefile for airflow-project:"
	@echo "  help                        Show this help message."
	@echo "  init                        Initialize Airflow (DB + user admin) and start Airflow - to be done only once."
	@echo "  up                          Start Airflow (postgres, scheduler, webserver)."
	@echo "  down                        Stop services (but keep volumes/data)."
	@echo "  reset                       Complete reset (remove volumes + re-init DB)."

init:
	$(DOCKER_COMPOSE) run --rm airflow-init
	$(DOCKER_COMPOSE) up -d

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

reset:
	$(DOCKER_COMPOSE) down -v
	$(DOCKER_COMPOSE) run --rm airflow-init
	$(DOCKER_COMPOSE) up -d
#!/bin/sh

echo "This script will generate the necessary files to run development docker."
echo "Run the build and the up the container by passing also the overrides file:\n"
echo "docker compose -f docker-compose.dev.yml build;"
echo "docker compose -f docker-compose.dev.yml up;"
echo "docker compose -f docker-compose.dev.yml exec cs-fastapi-pg-async-api-dev alembic upgrade head;"

echo "\nInitializing:"

echo "\t- Generate overrides files from templates"
cp backend_docker/config/.env.backend.dev.overrides.template backend_docker/config/.env.backend.dev.overrides
cp backend_docker/config/.env.postgres.dev.overrides.template backend_docker/config/.env.postgres.dev.overrides

echo "\t- Create folders"
mkdir -p ./docker_data_dev/backend/mediafiles
mkdir -p ./docker_data_dev/postgres/data
mkdir -p ./docker_data_dev/logs/backend

chmod 0750 ./docker_data_dev/postgres

echo "\nInitialization completed."

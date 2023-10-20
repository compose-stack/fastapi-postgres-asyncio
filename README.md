# FastAPI-Postgres-asyncio

FastAPI-Postgres-asyncio is a backend component for 
[`compose-stack`](https://github.com/compose-stack/compose-stack).

It includes the following packages:

- [`FastAPI`](https://fastapi.tiangolo.com/): Python web framework
- [`PostgreSQL`](https://www.postgresql.org/): World's most advanced relational DB
- [`SQLAlchemy 2`](https://www.sqlalchemy.org/): Python SQL toolkit
- [`Alembic`](https://alembic.sqlalchemy.org/en/latest/): SQLAlchemy migration tool
- [`AsyncPG`](https://magicstack.github.io/asyncpg/current/): Async PostgreSQL interface
- [`NewRelic`](https://newrelic.com/): Observability platform (to be added)

Additionally, it comes with built-in features:

- Users table with registration, verification, authentication and password reset
- Failed login limit to prevent password brute forcing
- Notifications (emails) setup and ready to be used with
  [MailerSend](https://www.mailersend.com/) (which has a generous free tier)
- Feature flags setup (one available, to control if new users can register or not)
- High test coverage with backend API tests

The out-of-the-box setup allows to prototype applications that requires users
registration quickly with latest technology based on Python and React.

## TL;DR

Development:

```bash
. backend_docker/initialise_dev.sh
docker compose -f docker-compose.dev.yml build
docker compose -f docker-compose.dev.yml up
docker compose -f docker-compose.dev.yml exec cs-fastapi-pg-async-api-dev alembic upgrade head
```

Test:

```bash
docker compose -f docker-compose.test.yml build
docker compose -f docker-compose.test.yml up --exit-code-from cs-fastapi-pg-async-api-test
```

## Installation

Requirements:

- `docker`
- (optional) a Python virtual environment (`compose-stack`) to initialise
  the services and for native VSCode environment

### Native Installation

```sh
python3 -m venv compose-stack
source compose-stack/bin/activate
pip install -r backend/requirements.txt -r backend/requirements_dev.txt
```

## Build & Run

### First run

The first time the containers are created the environment
needs to be setup.
Before running "build & run", run the following command:

```sh
. backend_docker/initialise_dev.sh
```

This commands creates the necessary folders mapped in the docker
configuration file.

### Backend

```sh
docker compose -f docker-compose.dev.yml build
docker compose -f docker-compose.dev.yml up
docker compose -f docker-compose.dev.yml exec ccs-fastapi-pg-async-api-dev alembic upgrade head
```

### Tests (great for TDD)

```sh
# run once or whenever a dependency change
docker compose -f docker-compose.test.yml build
# run the tests
docker compose -f docker-compose.test.yml up --exit-code-from cs-fastapi-pg-async-api-test
```

## System bootstrap

The bootstrap phase will:

- create Postgres database and tables

Run:

```sh
docker compose -f docker-compose.dev.yml exec cs-fastapi-pg-async-api-dev alembic upgrade head
```

## Backend documentation

Once the containers are built and the application is started,
the backend documentation should be available here:

[`http://localhost:8150/docs`](http://localhost:8150/docs)

# Production

#### To be completed

#### Note

The nginx configuration and environment variables are tailored to run on `compose-stack.com` domain,
so they need to be changed in order to work correctly with your domain.

## Debugging

Different containers can be debugged in different ways.

- To enter Postgres console, run:
  ```sh
  docker compose -f docker-compose.dev.yml exec compose-stack-postgres-dev bash
  > psql -h 127.0.0.1 -U postgres_user compose_stack
  ```

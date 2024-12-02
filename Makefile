# Docker settings
DOCKER_COMPOSE = docker compose
DOCKER_COMPOSE_RUN = $(DOCKER_COMPOSE) run --rm
DOCKER_COMPOSE_EXEC = $(DOCKER_COMPOSE) exec

# Container names
DJANGO_CONTAINER = django
CELERY_WORKER_CONTAINER = celery_worker
CELERY_BEAT_CONTAINER = celery_beat
POSTGRES_CONTAINER = coffee_shop_postgres
REDIS_CONTAINER = redis

# Build Docker containers
build:
	$(DOCKER_COMPOSE) build

# Up Docker containers
up:
	$(DOCKER_COMPOSE) up -d

# Run Docker containers
run:
	$(DOCKER_COMPOSE) up --build -d


# Stop the Docker containers
down:
	$(DOCKER_COMPOSE) down

# Remove volumes and clean up
clean:
	$(DOCKER_COMPOSE) down -v --rmi local --remove-orphans


# Create migrations in the Django container after DB changes
migrations:
	$(DOCKER_COMPOSE_EXEC) $(DJANGO_CONTAINER) python manage.py makemigrations

# Run migrations in the Django container
migrate:
	$(DOCKER_COMPOSE_EXEC) $(DJANGO_CONTAINER) python manage.py migrate

# Create static files in the Django container
collectstatic:
	$(DOCKER_COMPOSE_EXEC) $(DJANGO_CONTAINER) python manage.py collectstatic --noinput

# Create superuser in the Django container
createsuperuser:
	$(DOCKER_COMPOSE_EXEC) $(DJANGO_CONTAINER) python manage.py createsuperuser


# Start the Celery worker
celery-worker:
	$(DOCKER_COMPOSE) up -d celery_worker

# Start the Celery beat scheduler
celery-beat:
	$(DOCKER_COMPOSE) up -d celery_beat

# Stop Celery worker and beat
stop-celery:
	$(DOCKER_COMPOSE) down celery_worker celery_beat

# Execute a bash shell inside the Django container
shell:
	$(DOCKER_COMPOSE_EXEC) $(DJANGO_CONTAINER) /bin/bash

# View logs for all services
logs:
	$(DOCKER_COMPOSE) logs -f

# View logs for a specific service (e.g., Django or Celery)
logs-django:
	$(DOCKER_COMPOSE) logs -f $(DJANGO_CONTAINER)

logs-celery:
	$(DOCKER_COMPOSE) logs -f $(CELERY_WORKER_CONTAINER)

# First run: Build, up, apply migrations, and create superuser
first-run: build up migrate collectstatic createsuperuser

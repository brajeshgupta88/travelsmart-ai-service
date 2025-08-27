.PHONY: build test run

build:
	docker build -f docker/dockerfiles/Dockerfile -t travelsmart-ai-service:local .

dev:
	docker-compose up --build

test:
	pytest -q

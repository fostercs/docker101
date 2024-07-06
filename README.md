# Docker101

[Docker101 Image](https://hub.docker.com/r/fostercs/docker101)

`docker pull fostercs/docker101`

## Build via Compose
`docker compose up --build`

## Login
`docker login`

## Build
`docker build -t fostercs/docker101 .`

## List Images
`docker images`

## Publish Image
`docker push fostercs/docker101:latest`

## Run the repl
# CMD gunicorn 'app:app' --bind=0.0.0.0:8000
CMD ["python3", "map-filter-reduce.py"]

## Run the application
CMD gunicorn 'app:app' --bind=0.0.0.0:8000
# CMD ["python3", "map-filter-reduce.py"]
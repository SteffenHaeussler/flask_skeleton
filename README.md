# flask_skeleton
Simple flask skeleton for a stateless microservice (application for ml models, optimization, ...).
You can run the API locally in the develop environment using either by manually installing dependencies and running the app script in your shell or with Docker.

## Running service manually

To run the service manually in debug mode install the required python dependencies:

 `pip install -r requirements/develop.txt`

You can run the service in debug mode without gunicorn:

`./run_debug.sh`

## Running service in Docker

To build the Docker image:

`docker build -t "flask-api:latest" . --build-arg FLASK_ENV=develop`

To run the Docker image:

```
docker run \
  --env GITLAB_USERNAME=$GITLAB_USERNAME \
  --env GITLAB_PASSWORD=$GITLAB_PASSWORD \
  -p 5000:5000 -ti flask-api:latest
```

## Local querying

To check that the service is alive, run:

`curl -X GET "http://localhost:5000/health" -H  "accept: application/json"`

`curl -X GET "http://localhost:5000/v1/health" -H  "accept: application/json"`

## API Documentation

The user interface for the API is defined via Swagger in `swagger.yml` and exposed to the user via the `/docs` endpoint.

## Testing

To run unit tests:

`nosetests --with-coverage --cover-erase --cover-package=app app/tests`

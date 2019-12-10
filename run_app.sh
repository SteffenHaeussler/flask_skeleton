#!/bin/sh


if [ "$FLASK_ENV" == "prod" ]; then
	gunicorn manage:app -b :5000 -w 2 #--log-level error
elif [ "$FLASK_ENV" == "testing" ]; then
	pytest --cov-report html --cov=app app/tests
else
	gunicorn manage:app -b :5000 -w 2
fi

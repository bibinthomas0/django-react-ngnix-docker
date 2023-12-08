# Use the official Python image as the base image
FROM python:3.9

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app


CMD ["celery", "-A", "backend", "worker", "--loglevel=info"]
# CMD ["celery", "-A", "backend", "beat", "--loglevel=info"]
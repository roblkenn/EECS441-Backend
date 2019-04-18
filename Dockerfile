FROM python:3.6

RUN apt-get update && \
    apt-get install -y \
    python-opencv

RUN mkdir /app
WORKDIR /app
COPY . .

RUN pip install -r /app/requirements.txt

EXPOSE 80

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:80", "--timeout", "600", "application:app"]
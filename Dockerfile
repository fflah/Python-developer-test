FROM python:latest

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV="docker"

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
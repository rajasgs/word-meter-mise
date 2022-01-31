FROM python:3.9.5-slim-buster

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

# RUN apt update
# RUN apt install curl

RUN apt-get update
RUN apt-get -y install curl

CMD ["python", "app.py"]
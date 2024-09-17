FROM apache/airflow:latest

USER root


RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean

USER airflow

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

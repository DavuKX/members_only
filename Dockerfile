FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN pip install django
RUN pip install psycopg2-binary
RUN django-admin startproject members_only .
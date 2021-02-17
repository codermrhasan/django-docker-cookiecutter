# pull official base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /djangoproj
COPY requirements.txt /djangoproj/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /djangoproj/

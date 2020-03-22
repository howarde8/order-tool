FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /demo
WORKDIR /demo
COPY requirements.txt /demo/ 
RUN pip install -r requirements.txt


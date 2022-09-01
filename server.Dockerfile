FROM python:latest as base
COPY ./server /app/server
WORKDIR /app/server
RUN pip3 install -r requirements.txt
CMD python3 ./server.py

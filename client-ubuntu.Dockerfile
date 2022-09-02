FROM ubuntu:latest as base
RUN apt-get update
RUN apt-get install python3 wget net-tools -y
COPY ./client /app/client
WORKDIR /app/client
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py
RUN pip3 install -r requirements.txt
RUN apt-get -y install cron
RUN crontab -l | { cat; echo "*/45 * * * * python3 agent.py"; } | crontab -
CMD [ "sleep", "10000000", "&&", "cron" ]
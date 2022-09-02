FROM redhat/ubi8:latest as base
RUN dnf install python3 net-tools procps -y
COPY ./client /app/client
WORKDIR /app/client
RUN python3 -m ensurepip --upgrade
RUN pip3 install -r requirements.txt
RUN dnf install crontabs -y
RUN crontab -l | { cat; echo "*/45 * * * * python3 agent.py"; } | crontab -
CMD [ ["sleep", "10000000", "&&", "cron"] ]
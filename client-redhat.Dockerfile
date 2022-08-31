FROM redhat/ubi8:latest as base
RUN dnf install python3 net-tools procps -y
COPY ./client /app/client
WORKDIR /app/client
RUN python3 -m ensurepip --upgrade
RUN pip3 install -r requirements.txt
CMD [ "sleep", "10000000" ]
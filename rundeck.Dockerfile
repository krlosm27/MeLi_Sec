FROM rundeck/rundeck:3.4.10-20220118 as base
RUN dnf install python3 net-tools procps -y
CMD [ "sleep", "10000000" ]

FROM rundeck/rundeck:SNAPSHOT 

USER root

# upgrade os
RUN apt-get -y update && \
   apt-get -y install \
   software-properties-common 
 
# install python
RUN apt-get -y install python3-pip && \
   pip3 install --upgrade pip

RUN password rundeck:rundeck

USER rundeck

FROM mageai/mageai:latest
ARG PROJECT_NAME=ski_resort_weather 
ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}
COPY requirements.txt ${USER_CODE_PATH}/requirements.txt


RUN echo 'deb http://deb.debian.org/debian bullseye main' > /etc/apt/sources.list.d/bullseye.list
RUN apt-get update -y
RUN apt-get install -y openjdk-11-jdk
RUN rm /etc/apt/sources.list.d/bullseye.list
RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
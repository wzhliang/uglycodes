FROM ubuntu:17.10

RUN apt-get update && \
    apt-get install -y python3 &&  \
    apt-get install -y python3-pip &&  \
    pip3 install black && \
    apt-get install -y git && \
    apt-get install -y golang-go &&\
    apt-get install -y openjdk-9-jre-headless

ADD https://github.com/google/google-java-format/releases/download/google-java-format-1.6/google-java-format-1.6-all-deps.jar /tools/google-java-format-1.6-all-deps.jar
ADD main.py /tools

ENV PYTHONUNBUFFERED 0
CMD ['python', '/tools/main.py']

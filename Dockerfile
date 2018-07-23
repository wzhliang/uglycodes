FROM ubuntu:17.10

ADD https://github.com/google/google-java-format/releases/download/google-java-format-1.6/google-java-format-1.6-all-deps.jar /tools/google-java-format-1.6-all-deps.jar
RUN apt-get update && \
    apt-get install -y python3 &&  \
    apt-get install -y python3-pip &&  \
    pip3 install black && \
    apt-get install -y git && \
    apt-get install -y golang-go && \
    apt-get install -y openjdk-9-jre-headless && \
    apt-get install -y dos2unix && \
    ln -s /usr/bin/python3 /usr/bin/python

ADD main.py /tools

ENV PYTHONUNBUFFERED 0
CMD ['python', '/tools/main.py']

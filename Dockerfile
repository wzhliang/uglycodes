FROM java:8

RUN apt-get update && \
    apt-get install python3 &&  \
	pip3 install black && apt-get install git && apt-get install go
ADD https://github.com/google/google-java-format/releases/download/google-java-format-1.6/google-java-format-1.6-all-deps.jar /tools/google-java-format-1.6-all-deps.jar
ADD main.py /tools

ENV PYTHONUNBUFFERED 0
CMD ['python', '/tools/main.py']

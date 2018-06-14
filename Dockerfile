FROM python:3.6-alpine

ADD https://github.com/google/google-java-format/releases/download/google-java-format-1.6/google-java-format-1.6-all-deps.jar /tools/google-java-format-1.6-all-deps.jar
RUN pip install black && apk update && apk add git && apk add go
ADD main.py /tools

CMD ['python', '/tools/main.py']

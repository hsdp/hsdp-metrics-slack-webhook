FROM python:3.9-alpine
ADD ./application/ /application
COPY requirements.txt /tmp
COPY entrypoint.sh /entrypoint.sh
RUN /sbin/apk update && \
      /sbin/apk add --no-cache --virtual build-deps build-base linux-headers && \
      /usr/local/bin/pip3 install -r /tmp/requirements.txt && \
      /sbin/apk del build-deps && \
      /bin/rm -rf /var/cache/apk/*
EXPOSE 8080
STOPSIGNAL SIGINT
ENTRYPOINT /entrypoint.sh

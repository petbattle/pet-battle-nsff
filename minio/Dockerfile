FROM minio/minio
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Australia/Sydney /etc/localtime
ENV TZ="Australia/Sydney"
RUN echo "Australia/Sydney" >  /etc/timezone
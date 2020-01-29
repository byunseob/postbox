FROM python:3.7-alpine
MAINTAINER byunseob <byunseob2dev@gmail.com>

ENV HOME /svc

RUN apk --update add \
        bash \
        gcc \
        zlib-dev \
        git \
        linux-headers \
        build-base \
        musl \
        musl-dev \
        pcre-dev

RUN mkdir -p ${HOME}
RUN touch /svc/master.fifo

WORKDIR ${HOME}

ADD ./requirements.txt ${HOME}
RUN pip3.7 install -r requirements.txt
RUN pip3.7 install uwsgi

COPY . ${HOME}

ENTRYPOINT ["uwsgi", "--ini", "/svc/uwsgi.ini"]

EXPOSE ${PORT}
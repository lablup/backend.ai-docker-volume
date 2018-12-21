FROM ubuntu:18.04
MAINTAINER Jonghyun Park <adrysn@gmail.com>

RUN set -x; \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

ENV VERSION master
ENV PKGNAME backend.ai-docker-volume

COPY entrypoint.sh /
COPY . /${PKGNAME}

RUN mkdir -p /run/docker/plugins
RUN cd /${PKGNAME} \
    && pip3 install -U pip setuptools \
    && python3 setup.py install

ENTRYPOINT ["/entrypoint.sh"]

FROM ubuntu:18.04
MAINTAINER Jonghyun Park <adrysn@gmail.com>

RUN set -x; \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
        python3-setuptools \
        unzip \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /run/docker/plugins

ENV VERSION master
ENV PKGNAME backend.ai-docker-volume
RUN curl -o ${PKGNAME}.zip -SL https://github.com/lablup/${PKGNAME}/archive/${VERSION}.zip \
    && unzip ${PKGNAME}.zip \
    && rm ${PKGNAME}.zip \
    && mv ${PKGNAME}-${VERSION} ${PKGNAME} \
    && cd ${PKGNAME} \
    && python3 setup.py install \
    && cd .. \
    && rm -rf ${PKGNAME}

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
# CMD [""]

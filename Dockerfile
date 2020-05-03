FROM python:3.6-stretch
LABEL mantainer="ymussi@gmail.com"
LABEL fileversion=v0.1

WORKDIR /app/covid/

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y uwsgi-plugin-python3 git && \
    pip install --upgrade pip

COPY . .

ARG RUN_ENVIRONMENT
ENV PYTHONUNBUFFERED=0
ENV DBENV=${RUN_ENVIRONMENT}

RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update -y && apt install -y uwsgi uwsgi-src uuid-dev libcap-dev

RUN export PYTHON=python3.6 && \
    uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python36" && \
    mv python36_plugin.so /usr/lib/uwsgi/plugins/python36_plugin.so && \
    chmod 644 /usr/lib/uwsgi/plugins/python36_plugin.so

RUN pip install -r requirements.txt && \
    python setup.py develop

ENTRYPOINT ["/bin/sh","/app/covid/entrypoint.sh"]
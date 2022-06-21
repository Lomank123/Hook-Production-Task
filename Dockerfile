FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./spinwheel /spinwheel

WORKDIR /spinwheel

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev linux-headers python3-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home spinwheel && \
    mkdir -p /vol/web/static && \
    chown -R spinwheel:spinwheel /vol

ENV PATH="/py/bin:/py/lib:$PATH"

USER spinwheel

FROM python:3-alpine

LABEL maintainer="José Carlos Paiva <josepaiva94@gmail.com>"
LABEL description="Base image of apiCy, containing no language models."


WORKDIR /app

COPY pyproject.toml .

RUN apk update && \
    apk add build-base gcc libc-dev libffi-dev openssl-dev python3-dev && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry && \
    poetry install

COPY src .

EXPOSE 8000

CMD ["poetry", "run", "hypercorn", "apicy.server:app", "--bind", "0.0.0.0:8000", "--reload"]

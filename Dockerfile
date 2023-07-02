FROM python:3.11-alpine AS builder

WORKDIR /tmp

ENV POETRY_VERSION=1.5.1

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-alpine

WORKDIR /app

ENV TZ="America/Sao_Paulo" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    USER=appuser

RUN adduser --disabled-password --gecos '' $USER && \
    apk add curl

COPY --from=builder /tmp/requirements.txt ./requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./financial-control ./financial-control

RUN chown -R $USER:$USER /app

USER $USER

CMD ["uvicorn", "financial-control.main:app", "--host", "0.0.0.0", "--workers", "4", "--port", "8080", "--proxy-headers"]
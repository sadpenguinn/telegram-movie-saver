FROM python:3.9-slim as compiler
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install gcc

WORKDIR /app/

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

FROM python:3.9-slim as runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"


COPY main.py /app/
COPY model /app/model
COPY integration /app/integration

ENTRYPOINT ["python3", "/app/main.py"]

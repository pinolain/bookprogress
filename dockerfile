
FROM python:3.11.0-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
   && apt-get install -y python3-dev gcc musl-dev libffi-dev netcat

RUN pip install --upgrade pip



COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
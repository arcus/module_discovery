FROM python:3.9-slim-buster

ENV DASH_DEBUG_MODE False
COPY . /app
WORKDIR /app
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8050
CMD gunicorn -b 0.0.0.0:8050 --reload app:server
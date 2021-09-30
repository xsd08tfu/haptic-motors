FROM --platform=linux/arm python:alpine
ENV PYTHONUNBUFFERED=0
ENTRYPOINT ['python3','test.py']
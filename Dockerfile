FROM --platform=linux/arm python:alpine
ENTRYPOINT ["python3","test.py"]
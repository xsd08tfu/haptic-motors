FROM --platform=linux/arm python:alpine
ENTRYPOINT ["python3","-u","test.py"]
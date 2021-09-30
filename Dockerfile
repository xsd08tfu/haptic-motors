FROM --platform=linux/arm python:alpine

COPY code code

CMD ["/code/main.py"]

ENTRYPOINT ["python3"]
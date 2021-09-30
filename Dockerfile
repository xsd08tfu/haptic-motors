FROM --platform=linux/arm python:alpine

COPY code code

CMD ["/code/test.py"]

ENTRYPOINT ["python3"]
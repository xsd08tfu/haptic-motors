FROM --platform=linux/arm python:alpine

COPY code code

CMD ["ls"]
ENTRYPOINT []
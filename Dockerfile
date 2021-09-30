FROM --platform=linux/arm python:alpine

COPY code code

CMD ["cd code && ls"]

ENTRYPOINT []
FROM --platform=linux/arm python:alpine
CMD ["code/test.py"]
ENTRYPOINT ["python3"]
FROM python:3.13-alpine

WORKDIR /app

COPY test.py .

CMD ["python", "test.py"]

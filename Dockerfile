FROM python:3.11-slim

WORKDIR /root

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "./src/main.py"]

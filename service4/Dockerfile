FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]
COPY . .
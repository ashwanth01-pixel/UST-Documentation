FROM python:3.9-slim
WORKDIR /app
COPY client/client.py .
RUN pip install requests
CMD ["python", "client.py"]

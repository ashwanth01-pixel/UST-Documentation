FROM python:3.9-slim
WORKDIR /app
COPY server/server.py .
CMD ["python", "server.py"]

# 🐳 Docker Network Demo (Python Client-Server)

This demo shows how to use Docker networking to allow a Python client container to communicate with a Python server container using container names.

## 📁 Project Structure

```
docker-network-demo/
├── server/
│   └── server.py
├── client/
│   └── client.py
├── server.Dockerfile
├── client.Dockerfile
```

## 🛠 Build Docker Images

```bash
docker build -t server-image -f server.Dockerfile .
```
👉 Builds the server image from `server.Dockerfile`.

```bash
docker build -t client-image -f client.Dockerfile .
```
👉 Builds the client image from `client.Dockerfile`.

## 🌐 Create Docker Network

```bash
docker network create demo-net
```
👉 Creates a custom Docker bridge network named `demo-net`.

## 🚀 Run Server Container

```bash
docker run -d --name server-container --network demo-net server-image
```
👉 Runs the server container in detached mode, connects it to `demo-net`, and names it `server-container`.

## 📡 Run Client Container

```bash
docker run --rm --name client-container --network demo-net client-image
```
👉 Runs the client container (which sends a request to `server-container`), connects it to `demo-net`, and auto-removes it after completion.

## ✅ Expected Output

```text
Response from server: Hello from Server!
```

## 🧠 Key Point

Docker's custom network (`demo-net`) allows containers to **resolve each other by name** and communicate directly without using IP addresses.


# 🚀 Docker Volume Example with Python

This project demonstrates how to use **Docker volumes** to run a Python program (`print("hello world")`) in a clean and reusable way.

---

## 🧪 Commands Summary

```bash
# 🔧 Step 1: Build the Docker image from Dockerfile
docker build -t python-volume-image .

# 📦 Step 2: Create a named Docker volume for persistent storage
docker volume create docker-volume

# 📁 Step 3: Copy main.py into the Docker volume using a temporary Alpine container
docker run --rm -v docker-volume:/data -v $(pwd):/source alpine cp /source/main.py /data/

# 🚀 Step 4: Run the Python program from the volume using the built image
docker run --rm -v docker-volume:/data python-volume-image
```

---

## ✅ Output

```
hello world
```

---

## 📚 What’s Happening

- `docker build` creates an image that runs a Python script.
- `docker volume create` sets up persistent storage.
- `cp` command places your script inside the volume.
- `docker run` executes the script from the volume.

---

## 💡 Bonus Tips

- Use `docker volume ls` to list volumes.
- Use `docker volume inspect docker-volume` to check volume details.
- Use `docker run -it -v docker-volume:/data alpine sh` to explore contents.

---

Happy Dockering! 🐳

### 🧪 **DevOps Intern Assignment: Nginx Reverse Proxy + Docker**

# 🚀 Multi-Service App with Nginx Reverse Proxy

This project demonstrates a microservices setup using:

- 🐳 Docker Compose for container orchestration  
- 🌐 Nginx as a reverse proxy  
- ⚙️ Service 1 built with Go  
- 🐍 Service 2 built with Flask (Python)  

---

## 📁 Project Structure

![image](https://github.com/user-attachments/assets/e4516817-9678-4c00-b0c5-f989a40650a0)


4 directories, 10 files

---

## 🔧 Prerequisites

- Docker and Docker Compose installed
- Internet connection to pull base images

---

## 🔄 Step-by-Step Setup

### 1️⃣ Service 1 (Go)

- Handles routes: `/`, `/hello`, `/ping`
- Logs service status and errors to console

**Files:**
- `main.go`: Implements HTTP handlers
- `Dockerfile`: Builds Go binary and runs it

```bash
# Inside service_1 folder
docker build -t service1-go .
```

---

### 2️⃣ Service 2 (Python Flask)

- Handles routes: `/`, `/hello`, `/ping`
- Uses `Flask` with `uvicorn` server (based on pyproject.toml and uv.lock)

**Files:**
- `app.py`: Flask app
- `Dockerfile`: Installs dependencies & runs app
- `pyproject.toml`: Poetry-managed dependencies

```bash
# Inside service_2 folder
docker build -t service2-flask .
```

---

### 3️⃣ Nginx Reverse Proxy

- Forwards traffic:
  - `/service1/` → Service 1 (port 8001)
  - `/service2/` → Service 2 (port 8002)
- Logs HTTP requests and errors

**Files:**
- `nginx.conf`: Routing rules
- `Dockerfile`: Builds custom nginx image

---

## 📦 Compose Everything Together

From the root directory:

```bash
docker-compose up --build
```

Once running, access:

- `http://<EC2-IP>:8080/service1/hello`
- `http://<EC2-IP>:8080/service2/hello`

---

## ✅ Features Implemented

- [x] Logging in Go and Python apps
- [x] Clean modular Docker setup for each service
- [x] Centralized reverse proxy
- [x] Health routes for automation (`/ping`)

---

## 📄 Author

G. Gowtham — DevOps & AWS Cloud Enthusiast  




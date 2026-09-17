# 🧩 Sudoku DevOps

A Python Flask-based Sudoku web application built as a hands-on project to learn and implement **DevOps practices**.

The project covers the complete flow from development and testing to containerization and CI/CD deployment.

---

## 🚀 Features

- Interactive 9×9 Sudoku board
- Random Sudoku puzzle generation
- Backtracking-based Sudoku solver
- Player move validation
- Mistake counter with 3-mistake game over
- Complete solution validation
- Automated testing with Pytest
- Dockerized application with Gunicorn
- Jenkins CI/CD pipeline
- Docker Hub image registry
- Docker Compose deployment
- Versioned Docker images using Jenkins build numbers

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Testing | Pytest |
| Containerization | Docker, Docker Compose |
| Server | Gunicorn |
| CI/CD | Jenkins |
| Registry | Docker Hub |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```text
sudoku-devops/
│
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── routes.py
│   └── sudoku.py
│
├── tests/
│   └── test_sudoku.py
│
├── jenkins/
│   └── Dockerfile
│
├── Dockerfile
├── Jenkinsfile
├── compose.yaml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

## 🧪 Testing

Run the test suite with:

```bash
python -m pytest
```

Current result:

```text
16 passed
```

---

## 🐳 Run with Docker

### Build

```bash
docker build -t sudoku-devops .
```

### Run

```bash
docker run -d -p 5000:5000 --name sudoku-app sudoku-devops
```

Open:

```text
http://localhost:5000
```

---

## 🔄 CI/CD Pipeline

```text
GitHub
   ↓
Jenkins
   ↓
Run Tests
   ↓
Build Docker Image
   ↓
Push to Docker Hub
   ↓
Docker Compose
   ↓
Deploy Application
```

Each Jenkins build creates a versioned Docker image:

```text
vivekyadavdocker/sudoku-devops:<BUILD_NUMBER>
```

---

## 🎯 DevOps Concepts Demonstrated

- Version Control
- Automated Testing
- Containerization
- CI/CD
- Pipeline as Code
- Container Registry
- Automated Deployment
- Docker Compose
- Build Versioning

---

## 📌 Future Learning

- Kubernetes
- AWS Deployment
- Terraform
- Prometheus
- Grafana
- Kubernetes Health Checks

---

## 👨‍💻 Author

**Vivek Yadav**

GitHub: [VivekYadavOnGit](https://github.com/VivekYadavOnGit)

Repository: [Sudoku DevOps](https://github.com/VivekYadavOnGit/sudoku-devops)

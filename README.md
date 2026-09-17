# 🧩 Sudoku DevOps

A Python Flask-based Sudoku web application built as a hands-on project for learning **software development, testing, Git, Docker, Jenkins, CI/CD, Docker Compose, Docker Hub, and DevOps practices**.

The project is being developed incrementally, with the goal of eventually implementing a complete local **CI/CD and production-like environment using Docker, Jenkins, Docker Compose, Kubernetes, and monitoring tools**—without requiring AWS.

---

## 🚧 Project Status

**Current stage:** Application + Automated Testing + Git/GitHub + Docker + Gunicorn + Jenkins CI/CD + Docker Hub + Docker Compose

### Completed

* [x] Python Sudoku solver
* [x] Sudoku validation logic
* [x] Flask web application
* [x] Interactive 9×9 Sudoku board
* [x] Solution validation API
* [x] Automated tests using Pytest
* [x] Python virtual environment
* [x] Git repository
* [x] Initial Git commit
* [x] GitHub repository
* [x] Dockerized application
* [x] Production and development dependency separation
* [x] Gunicorn production WSGI server
* [x] Docker port mapping
* [x] `.dockerignore`
* [x] Jenkins CI pipeline
* [x] Jenkins Docker integration
* [x] Automated dependency installation in CI
* [x] Automated test execution in CI
* [x] Automated Docker image builds
* [x] Jenkinsfile / Pipeline as Code
* [x] Jenkins pipeline stored and version-controlled in GitHub
* [x] Docker image versioning using Jenkins build numbers
* [x] Docker Hub integration
* [x] Secure Docker Hub credentials in Jenkins
* [x] Automated Docker image push to Docker Hub
* [x] Docker Compose deployment
* [x] Automated local deployment using Jenkins
* [x] End-to-end CI/CD pipeline

### Coming Next

* [ ] Improve Sudoku game functionality
* [ ] Generate random Sudoku puzzles
* [ ] Add difficulty levels
* [ ] Improve frontend UI/UX
* [ ] Improve deployment/container lifecycle handling
* [ ] Kubernetes deployment
* [ ] Kubernetes Services
* [ ] ConfigMaps and Secrets
* [ ] Kubernetes health checks
* [ ] Prometheus monitoring
* [ ] Grafana dashboards
* [ ] Complete local production-like DevOps environment

---

## 🛠️ Tech Stack

### Application

* **Python**
* **Flask**
* **HTML**
* **CSS**
* **JavaScript**

### Testing

* **Pytest**

### Version Control

* **Git**
* **GitHub**

### Containerization

* **Docker**
* **Docker Compose**
* **Gunicorn**

### CI/CD

* **Jenkins**
* **Jenkins Pipeline**
* **Jenkinsfile / Pipeline as Code**

### Container Registry

* **Docker Hub**

### Planned DevOps Tools

* **Kubernetes**
* **Prometheus**
* **Grafana**

---

## 📁 Project Structure

```text
sudoku-devops/
│
├── app/
│   ├── __init__.py
│   ├── sudoku.py
│   ├── routes.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── style.css
│       └── script.js
│
├── tests/
│   └── test_sudoku.py
│
├── jenkins/
│   └── Dockerfile
│
├── run.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── Jenkinsfile
├── compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ⚙️ Current Features

### Sudoku Solver

The application contains a Python-based Sudoku engine using a **backtracking algorithm**.

The solver can:

* Find empty cells
* Validate possible moves
* Check rows
* Check columns
* Check 3×3 boxes
* Solve the Sudoku puzzle

### Web Application

The Flask application provides:

* A 9×9 Sudoku board
* Pre-filled puzzle numbers
* Editable cells
* Check Solution functionality
* Backend solution validation

### API

The application currently exposes:

```text
POST /check
```

The endpoint accepts a Sudoku board and validates whether the submitted solution is correct.

---

## 🧪 Testing

The project uses **Pytest** for automated testing.

Current test coverage includes:

* Valid Sudoku moves
* Invalid row moves
* Invalid column moves
* Sudoku solving
* Incomplete solutions
* Correct solutions
* Incorrect solutions
* Invalid board dimensions

Run the tests locally with:

```powershell
python -m pytest
```

Current result:

```text
8 passed
```

### Jenkins Automated Testing

Jenkins automatically runs the test suite inside a `python:3.14-slim` Docker environment.

The CI pipeline verifies that the application passes all automated tests before proceeding to the Docker image build and deployment stages.

Current CI result:

```text
8 passed
```

---

## 🐳 Docker

The application is containerized using Docker.

The production container uses **Gunicorn** as the WSGI server instead of Flask's development server.

### Build the Docker image

```powershell
docker build -t sudoku-devops .
```

### Run the container

```powershell
docker run -d -p 5000:5000 --name sudoku-app sudoku-devops
```

The application will be available at:

```text
http://localhost:5000
```

### Check running containers

```powershell
docker ps
```

### View container logs

```powershell
docker logs sudoku-app
```

### Stop the container

```powershell
docker stop sudoku-app
```

### Remove the container

```powershell
docker rm sudoku-app
```

### Docker Image

The production Docker image uses `python:3.14-slim` as its base image.

The image includes only production dependencies from `requirements.txt`. Development tools such as Pytest are kept separate.

---

## 📦 Dependencies

Production and development dependencies are maintained separately.

### Production

`requirements.txt` contains only the dependencies required to run the application.

```text
Flask==3.1.3
gunicorn==23.0.0
```

### Development

`requirements-dev.txt` includes the production dependencies plus Pytest.

```text
-r requirements.txt
pytest==9.1.1
```

This prevents development-only tools such as Pytest from being installed into the production Docker image.

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/VivekYadavOnGit/sudoku-devops.git
cd sudoku-devops
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install development dependencies

```powershell
python -m pip install -r requirements-dev.txt
```

### 5. Run tests

```powershell
python -m pytest
```

### 6. Run the application

```powershell
python run.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## 🐳 Docker Compose

Docker Compose is used to deploy the versioned Docker image.

The application image is configured through the `IMAGE_TAG` environment variable.

Example:

```powershell
$env:IMAGE_TAG="16"
docker compose up -d
```

Check the deployment:

```powershell
docker compose ps
```

Stop the Compose deployment:

```powershell
docker compose down
```

The Compose deployment uses the Docker Hub image:

```text
vivekyadavdocker/sudoku-devops:${IMAGE_TAG}
```

---

## 🔄 Development Workflow

The project is being developed using an incremental workflow:

```text
Write Code
    ↓
Write Tests
    ↓
Run Tests
    ↓
Find Bugs
    ↓
Fix Bugs
    ↓
Run Tests Again
    ↓
Git Commit
    ↓
Git Push
    ↓
GitHub
```

The automated CI/CD workflow is:

```text
Developer
    ↓
Git Commit
    ↓
Git Push
    ↓
GitHub
    ↓
Jenkins
    ↓
Checkout
    ↓
Automated Tests
    ↓
Docker Image Build
    ↓
Docker Image Tag
    ↓
Docker Hub
    ↓
Docker Compose Deployment
    ↓
Sudoku Application 🚀
```

Each Jenkins build produces a versioned Docker image using the Jenkins build number.

For example:

```text
Build #14
    ↓
vivekyadavdocker/sudoku-devops:14

Build #15
    ↓
vivekyadavdocker/sudoku-devops:15

Build #16
    ↓
vivekyadavdocker/sudoku-devops:16
```

This makes every CI build identifiable and allows different application versions to be tracked through their Docker image tags.

---

## 🔄 Jenkins CI/CD Pipeline

The Jenkins pipeline is defined using a **Jenkinsfile** stored in the GitHub repository.

This follows the **Pipeline as Code** approach.

### Pipeline stages

```text
Checkout
    ↓
Run Tests
    ↓
Build Docker Image
    ↓
Push to Docker Hub
    ↓
Deploy with Docker Compose
```

### 1. Checkout

Jenkins checks out the `main` branch from the GitHub repository.

### 2. Run Tests

Jenkins uses:

```text
python:3.14-slim
```

as the isolated test environment.

Development dependencies are installed and Pytest is executed.

```text
8 tests
   ↓
8 passed ✅
```

### 3. Build Docker Image

After successful tests, Jenkins builds the production Docker image:

```text
sudoku-devops:${BUILD_NUMBER}
```

For example:

```text
sudoku-devops:16
```

### 4. Push to Docker Hub

The versioned image is tagged with the Docker Hub repository:

```text
vivekyadavdocker/sudoku-devops:${BUILD_NUMBER}
```

Jenkins authenticates to Docker Hub using credentials stored securely in Jenkins.

The image is then pushed to Docker Hub.

### 5. Deploy

After the image is successfully pushed, Jenkins deploys the new image using Docker Compose.

The deployment uses:

```text
IMAGE_TAG=${BUILD_NUMBER}
```

For example, Jenkins build `#16` deploys:

```text
vivekyadavdocker/sudoku-devops:16
```

The application is exposed on:

```text
http://localhost:5000
```

---

## 📄 Jenkinsfile

The project's CI/CD pipeline is stored in:

```text
Jenkinsfile
```

Instead of keeping the pipeline configuration only inside Jenkins, the pipeline definition is version-controlled together with the application.

This provides:

* Version-controlled CI/CD configuration
* Reproducible pipeline configuration
* Easier Jenkins recovery
* Pipeline changes tracked through Git
* A single source of truth for the project workflow

---

## 🐳 Docker Hub

The project uses Docker Hub as its container registry.

Docker images produced by Jenkins are pushed using versioned tags:

```text
vivekyadavdocker/sudoku-devops:14
vivekyadavdocker/sudoku-devops:15
vivekyadavdocker/sudoku-devops:16
```

This separates the **build process** from the **deployment process**:

```text
Jenkins
   ↓
Build Image
   ↓
Push Image
   ↓
Docker Hub
   ↓
Pull Image
   ↓
Docker Compose
   ↓
Run Application
```

---

## 🎯 Learning Goals

This project is being developed primarily as a **hands-on DevOps learning project**.

The goal is to understand how development and operations work together by taking one application through the entire lifecycle:

```text
Application Development
        ↓
Testing
        ↓
Version Control
        ↓
Containerization
        ↓
Continuous Integration
        ↓
Container Registry
        ↓
Continuous Delivery
        ↓
Deployment
        ↓
Monitoring
```

The CI/CD environment initially runs **locally**, without depending on AWS or another cloud provider.

---

## 📌 Project Philosophy

Instead of learning DevOps tools independently, this project uses a single application to understand how the tools work together.

For example:

```text
Git
 ↓
Version control

Pytest
 ↓
Automated testing

Docker
 ↓
Containerization

Gunicorn
 ↓
Production WSGI server

Jenkins
 ↓
CI/CD automation

Jenkinsfile
 ↓
Pipeline as Code

Docker Hub
 ↓
Container Registry

Docker Compose
 ↓
Application Deployment

Kubernetes
 ↓
Container orchestration

Prometheus + Grafana
 ↓
Monitoring
```

Each tool will be introduced only when there is a practical reason to use it.

---

## 🏁 Current Milestone

The project has successfully progressed from a basic Flask application to a **local automated CI/CD pipeline with Docker Hub and Docker Compose deployment**.

Current workflow:

```text
GitHub
   ↓
Jenkins
   ↓
Checkout
   ↓
Python Docker Environment
   ↓
8 Automated Tests
   ↓
Docker Image Build
   ↓
Versioned Docker Image
   ↓
Docker Hub
   ↓
Docker Compose
   ↓
Local Deployment
   ↓
Sudoku Application 🚀
```

The latest successful Jenkins build demonstrates the complete workflow:

```text
Jenkins Build #16
      ↓
8 Tests Passed
      ↓
Docker Image Built
      ↓
Image :16
      ↓
Pushed to Docker Hub
      ↓
Docker Compose Deployment
      ↓
sudoku-app Running
```

---

## 👨‍💻 Project Status

This project is actively being developed as part of a hands-on DevOps learning journey.

The application is currently:

* **Containerized**
* **Running with Gunicorn**
* **Covered by 8 automated tests**
* **Integrated with GitHub**
* **Automatically tested by Jenkins**
* **Automatically built into a Docker image**
* **Versioned using Jenkins build numbers**
* **Pushed automatically to Docker Hub**
* **Deployed automatically using Docker Compose**
* **Using a version-controlled Jenkinsfile**

### Next Phase

The next major phase is **Kubernetes**.

Planned progression:

```text
Docker
   ↓
Jenkins CI/CD
   ↓
Docker Hub
   ↓
Docker Compose
   ↓
Kubernetes
   ↓
Services
   ↓
ConfigMaps & Secrets
   ↓
Health Checks
   ↓
Prometheus
   ↓
Grafana
```

The long-term goal is to build a complete **local production-like DevOps environment** around the Sudoku application.
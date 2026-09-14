# 🧩 Sudoku DevOps

A Python Flask-based Sudoku web application built as a hands-on project for learning **software development, testing, Git, Docker, Jenkins, CI/CD, and DevOps practices**.

The project is being developed incrementally, with the goal of eventually implementing a complete local **CI/CD pipeline using Docker, Jenkins, Kubernetes, and monitoring tools**—without requiring AWS.

---

## 🚧 Project Status

**Current stage:** Application + Automated Testing + Git/GitHub + Docker + Gunicorn + Jenkins CI/CD

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
* [x] Local automated deployment using Jenkins
* [x] Jenkinsfile / Pipeline as Code
* [x] Jenkins pipeline stored and version-controlled in GitHub

### Coming Next

* [ ] Improve Sudoku game functionality
* [ ] Generate random Sudoku puzzles
* [ ] Add difficulty levels
* [ ] Improve frontend UI/UX
* [ ] Docker Compose
* [ ] Docker image tagging and version management
* [ ] Docker Hub / Container Registry
* [ ] Secure Jenkins credentials
* [ ] Kubernetes deployment
* [ ] Kubernetes Services
* [ ] ConfigMaps and Secrets
* [ ] Kubernetes health checks
* [ ] Prometheus monitoring
* [ ] Grafana dashboards
* [ ] Complete local production-like CI/CD environment

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
* **Gunicorn**

### CI/CD

* **Jenkins**
* **Jenkins Pipeline**
* **Jenkinsfile / Pipeline as Code**

### Planned DevOps Tools

* **Docker Compose**
* **Docker Hub**
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
├── run.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── Jenkinsfile
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

Jenkins automatically runs the test suite using a `python:3.14-slim` Docker environment.

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

The current production Docker image is approximately **214 MB** using `python:3.14-slim`.

The project intentionally uses a slim Python base image and separates production dependencies from development dependencies.

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
git clone <repository-url>
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
GitHub
```

The current automated CI/CD workflow is:

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
Local Deployment
    ↓
Sudoku Application
```

The Docker image produced by each Jenkins build is tagged using the Jenkins build number.

For example:

```text
sudoku-devops:7
sudoku-devops:8
sudoku-devops:9
```

This allows each CI build to produce an identifiable Docker image.

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
Deploy
```

### Run Tests

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

### Build Docker Image

After successful tests, Jenkins builds the production Docker image:

```text
sudoku-devops:${BUILD_NUMBER}
```

For example:

```text
sudoku-devops:8
```

### Deploy

After the image is built successfully, Jenkins:

1. Stops the existing `sudoku-app` container
2. Removes the old container
3. Creates a new container from the newly built image
4. Exposes the application on port `5000`

The resulting application is available locally at:

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

The project has successfully progressed from a basic Flask application to a **local automated CI/CD pipeline**.

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
Local Deployment
   ↓
Sudoku Application 🚀
```

The next major milestone is introducing a **Docker Registry**, allowing Jenkins to push versioned images to Docker Hub before moving toward Kubernetes-based deployment.

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
* **Automatically deployed locally by Jenkins**
* **Using a version-controlled Jenkinsfile**

The next phase will introduce **Docker Hub, image versioning, and Kubernetes**, progressively building toward a complete local DevOps environment.

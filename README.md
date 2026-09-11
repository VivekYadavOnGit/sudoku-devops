# 🧩 Sudoku DevOps

A Python Flask-based Sudoku web application built as a hands-on project for learning **software development, testing, Git, and DevOps practices**.

The project is being developed incrementally, with the goal of eventually implementing a complete local **CI/CD pipeline using Docker, Jenkins, and Kubernetes**—without requiring AWS.

---

## 🚧 Project Status

**Current stage:** Application + Automated Testing + Git/GitHub

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

### Coming Next

* [ ] Improve Sudoku game functionality
* [ ] Generate random Sudoku puzzles
* [ ] Add difficulty levels
* [ ] Improve frontend UI/UX
* [ ] Dockerize the application
* [ ] Docker Compose
* [ ] Jenkins CI pipeline
* [ ] Automated Docker image builds
* [ ] Docker Hub
* [ ] Kubernetes deployment
* [ ] Prometheus monitoring
* [ ] Grafana dashboards
* [ ] Complete local CI/CD pipeline

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

### Planned DevOps Tools

* **Docker**
* **Docker Compose**
* **Jenkins**
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

Run the tests with:

```powershell
python -m pytest
```

Current result:

```text
8 passed
```

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

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Run the application

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

The future DevOps workflow will extend this into:

```text
Developer
    ↓
Git Push
    ↓
GitHub
    ↓
Jenkins
    ↓
Automated Tests
    ↓
Docker Build
    ↓
Docker Registry
    ↓
Kubernetes
    ↓
Application
    ↓
Monitoring
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
Continuous Delivery
        ↓
Deployment
        ↓
Monitoring
```

The CI/CD environment will initially run **locally**, without depending on AWS or another cloud provider.

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

Jenkins
 ↓
CI/CD automation

Kubernetes
 ↓
Container orchestration

Prometheus + Grafana
 ↓
Monitoring
```

Each tool will be introduced only when there is a practical reason to use it.

---

## 👨‍💻 Project Status

This project is actively being developed as part of a hands-on DevOps learning journey.

More features and DevOps automation will be added progressively.
# 🚀 Sudoku DevOps — Interview Revision

A DevOps-focused interview revision guide based on the **Sudoku DevOps** project.

The goal is to understand not only what commands were used, but also why each tool was used, how the tools interact, common interview questions, failure scenarios, and troubleshooting.

---

# 📚 Table of Contents

1. [Project Architecture](#1-project-architecture)
2. [DevOps Workflow](#2-devops-workflow)
3. [Git](#3-git)
4. [GitHub](#4-github)
5. [CI/CD](#5-cicd)
6. [Jenkins](#6-jenkins)
7. [Jenkinsfile](#7-jenkinsfile)
8. [Jenkins Pipeline Stages](#8-jenkins-pipeline-stages)
9. [Jenkins Agents](#9-jenkins-agents)
10. [Jenkins Credentials](#10-jenkins-credentials)
11. [Docker](#11-docker)
12. [Dockerfile](#12-dockerfile)
13. [Docker Image](#13-docker-image)
14. [Docker Container](#14-docker-container)
15. [Docker Networking & Ports](#15-docker-networking--ports)
16. [.dockerignore](#16-dockerignore)
17. [Gunicorn](#17-gunicorn)
18. [Docker Compose](#18-docker-compose)
19. [Environment Variables](#19-environment-variables)
20. [Docker Hub](#20-docker-hub)
21. [Image Tagging & Versioning](#21-image-tagging--versioning)
22. [Automated Testing](#22-automated-testing)
23. [CI/CD End-to-End Flow](#23-cicd-end-to-end-flow)
24. [Security](#24-security)
25. [Troubleshooting](#25-troubleshooting)
26. [Important Commands](#26-important-commands)
27. [Important DevOps Interview Questions](#27-important-devops-interview-questions)
28. [Project-Based Interview Questions](#28-project-based-interview-questions)
29. [Common Follow-Up Questions](#29-common-follow-up-questions)
30. [Final Interview Checklist](#30-final-interview-checklist)

---

# 1. Project Architecture

## Project

**Sudoku DevOps**

The application is a Python Flask Sudoku application used to implement a practical DevOps workflow.

## Architecture

```text
                    ┌──────────────┐
                    │   Developer  │
                    └──────┬───────┘
                           │
                       Git Push
                           │
                           ▼
                    ┌──────────────┐
                    │    GitHub    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Jenkins   │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
           Checkout      Testing      Build
                                         │
                                         ▼
                                  Docker Image
                                         │
                                         ▼
                                  Docker Hub
                                         │
                                         ▼
                                Docker Compose
                                         │
                                         ▼
                                   Application
```

---

# 2. DevOps Workflow

The complete workflow is:

```text
Developer
   ↓
Write Code
   ↓
Git
   ↓
GitHub
   ↓
Jenkins
   ↓
Checkout
   ↓
Automated Tests
   ↓
Docker Build
   ↓
Docker Tag
   ↓
Docker Push
   ↓
Docker Hub
   ↓
Docker Compose
   ↓
Deployment
```

The most important thing to understand is **how these technologies connect**.

---

# 3. Git

Git is a distributed version-control system.

It tracks changes to source code.

## Why Git?

- Track code changes
- Maintain project history
- Create branches
- Revert changes
- Collaborate with developers
- Integrate with CI/CD

## Basic Workflow

```text
Working Directory
       ↓
Staging Area
       ↓
Git Repository
       ↓
Remote Repository
```

## Important Commands

### Check Status

```bash
git status
```

### Add Changes

```bash
git add .
```

### Commit

```bash
git commit -m "message"
```

### Push

```bash
git push origin main
```

### Pull

```bash
git pull
```

### View History

```bash
git log
```

---

## Interview Questions

### What is Git?

> Git is a distributed version-control system used to track source-code changes and manage different versions of a project.

### Git vs GitHub?

| Git | GitHub |
|---|---|
| Version-control tool | Hosting/collaboration platform |
| Runs locally | Cloud-based service |
| Tracks changes | Hosts Git repositories |
| CLI/tool | Web platform + Git services |

---

# 4. GitHub

GitHub hosts the project's Git repository.

Repository:

```text
https://github.com/VivekYadavOnGit/sudoku-devops
```

Branch:

```text
main
```

## Why GitHub in DevOps?

GitHub acts as the source-code repository from which Jenkins obtains the application source code.

```text
Developer
    ↓
git push
    ↓
GitHub
    ↓
Jenkins
```

---

# 5. CI/CD

## Continuous Integration

CI means frequently integrating code changes and automatically validating them.

In this project:

```text
GitHub
   ↓
Jenkins
   ↓
Checkout
   ↓
Install Dependencies
   ↓
Run Tests
```

## Continuous Delivery / Deployment

After validation:

```text
Tests Pass
   ↓
Docker Build
   ↓
Docker Hub
   ↓
Deployment
```

## CI vs CD

| CI | CD |
|---|---|
| Integrate code | Deliver/deploy application |
| Run tests | Build artifacts/images |
| Detect bugs early | Publish and deploy |
| Validate changes | Release changes |

---

# 6. Jenkins

Jenkins is an automation server used to implement CI/CD pipelines.

In this project Jenkins automates:

```text
Checkout
   ↓
Testing
   ↓
Docker Build
   ↓
Docker Push
   ↓
Deployment
```

## Why Jenkins?

Without Jenkins:

```text
Developer
   ↓
Manually run tests
   ↓
Manually build image
   ↓
Manually push image
   ↓
Manually deploy
```

With Jenkins:

```text
Git Push
   ↓
Automated Pipeline
   ↓
Application Deployment
```

---

# 7. Jenkinsfile

The pipeline is defined in:

```text
Jenkinsfile
```

This is called:

## Pipeline as Code

The CI/CD configuration is stored alongside the application source code.

### Advantages

- Version controlled
- Reproducible
- Easy to review
- Changes tracked in Git
- Easier Jenkins recovery
- Pipeline configuration becomes part of the project

---

# 8. Jenkins Pipeline Stages

The project pipeline contains:

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

## Stage 1 — Checkout

Jenkins checks out the source code from GitHub.

```groovy
git branch: 'main',
    url: 'https://github.com/VivekYadavOnGit/sudoku-devops.git'
```

### Interview Question

**Why does Jenkins need Checkout?**

> Jenkins needs the latest source code from the repository so that subsequent pipeline stages can test and build the current version of the application.

---

# 9. Jenkins Agents

Jenkins agents are machines or environments where pipeline steps execute.

The test stage uses:

```groovy
agent {
    docker {
        image 'python:3.14-slim'
    }
}
```

Therefore tests run inside a Python Docker environment.

## Why?

It provides an isolated and predictable environment.

```text
Jenkins
   ↓
Python Docker Environment
   ↓
Install Dependencies
   ↓
Run Pytest
```

---

# 10. Jenkins Credentials

Docker Hub credentials are stored in Jenkins.

Credential ID:

```text
dockerhub-credentials
```

The credentials are injected into the pipeline using:

```groovy
withCredentials(...)
```

## Why not hardcode credentials?

Never do:

```text
username = "myusername"
password = "mypassword"
```

inside a Jenkinsfile.

Instead:

```text
Jenkins Credentials
        ↓
Pipeline
        ↓
Docker Login
```

This keeps secrets outside source control.

---

# 11. Docker

Docker is a containerization platform.

It packages an application and its required environment into a container image.

## Why Docker?

It helps provide consistency between environments.

Without Docker:

```text
Developer Machine
     ↓
Different Python Version
     ↓
Different Dependencies
     ↓
"It works on my machine"
```

With Docker:

```text
Application
+
Dependencies
+
Runtime
      ↓
Docker Image
      ↓
Container
```

---

# 12. Dockerfile

The `Dockerfile` defines how the application image is built.

Important Dockerfile instructions:

```dockerfile
FROM
WORKDIR
COPY
RUN
EXPOSE
CMD
```

## `FROM`

Defines the base image.

This project uses:

```text
python:3.14-slim
```

## `WORKDIR`

Defines the working directory inside the image.

## `COPY`

Copies application files into the image.

## `RUN`

Executes commands during image creation.

## `EXPOSE`

Documents the port used by the application.

## `CMD`

Defines the default command used when the container starts.

---

# 13. Docker Image

A Docker image is a packaged, immutable template used to create containers.

Example:

```text
sudoku-devops:16
```

or:

```text
vivekyadavdocker/sudoku-devops:16
```

Think:

```text
Dockerfile
    ↓
docker build
    ↓
Docker Image
```

---

# 14. Docker Container

A container is a running instance of a Docker image.

```text
Docker Image
     ↓
docker run
     ↓
Container
```

Example:

```bash
docker run -d -p 5000:5000 --name sudoku-app sudoku-devops
```

## Image vs Container

| Image | Container |
|---|---|
| Template | Running instance |
| Immutable | Runtime environment |
| Used to create containers | Created from image |
| Stored locally/registry | Runs on Docker engine |

---

# 15. Docker Networking & Ports

The project uses:

```bash
-p 5000:5000
```

Format:

```text
HOST_PORT:CONTAINER_PORT
```

Therefore:

```text
Host
Port 5000
   ↓
Container
Port 5000
```

The application can be accessed through:

```text
http://localhost:5000
```

---

# 16. `.dockerignore`

`.dockerignore` prevents unnecessary files from being included in the Docker build context.

Typical examples:

```text
venv/
.git/
__pycache__/
.pytest_cache/
```

## Benefits

- Smaller build context
- Faster builds
- Cleaner image
- Prevents unnecessary files from being copied

---

# 17. Gunicorn

Gunicorn is a Python WSGI HTTP server.

The project uses Gunicorn instead of Flask's development server inside the production container.

## What is WSGI?

WSGI:

**Web Server Gateway Interface**

It defines how Python web applications communicate with web servers.

### Interview Answer

> "I used Gunicorn as the production WSGI server instead of Flask's built-in development server."

---

# 18. Docker Compose

Docker Compose allows application services to be defined declaratively in:

```text
compose.yaml
```

The project uses Compose for deployment.

Example:

```bash
docker compose up -d
```

## Why Compose?

It provides a repeatable way to start and manage the application's container.

Instead of remembering a long `docker run` command:

```text
compose.yaml
     ↓
docker compose up
     ↓
Application
```

---

# 19. Environment Variables

The deployment uses:

```text
IMAGE_TAG
```

Example:

```powershell
$env:IMAGE_TAG="16"
```

Compose then uses:

```text
vivekyadavdocker/sudoku-devops:${IMAGE_TAG}
```

which becomes:

```text
vivekyadavdocker/sudoku-devops:16
```

## Why use an environment variable?

It allows the deployment to select different image versions without changing the Compose file.

---

# 20. Docker Hub

Docker Hub is the container registry used by the project.

Repository:

```text
vivekyadavdocker/sudoku-devops
```

Jenkins pushes versioned images to Docker Hub.

```text
Jenkins
   ↓
Docker Build
   ↓
Docker Tag
   ↓
Docker Push
   ↓
Docker Hub
```

---

# 21. Image Tagging & Versioning

Jenkins provides:

```text
BUILD_NUMBER
```

Example:

```text
Build #16
```

The image becomes:

```text
sudoku-devops:16
```

and:

```text
vivekyadavdocker/sudoku-devops:16
```

## Why version images?

Versioning provides:

- Traceability
- Build identification
- Easier debugging
- Ability to distinguish releases
- Better deployment control

Example:

```text
Build #14 → Image :14
Build #15 → Image :15
Build #16 → Image :16
```

---

# 22. Automated Testing

The project uses:

```text
Pytest
```

Current test result:

```text
16 passed
```

## Why Automated Testing?

Automated tests help detect application problems before deployment.

Pipeline:

```text
Code
 ↓
Tests
 ↓
PASS
 ↓
Docker Build
 ↓
Deploy
```

If tests fail:

```text
Tests
 ↓
FAIL
 ↓
Pipeline Stops
```

This prevents the pipeline from continuing with invalid code.

---

# 23. CI/CD End-to-End Flow

This is the most important section to memorize.

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
Run Tests
    ↓
Tests Pass?
   ↙       ↘
 NO        YES
 ↓          ↓
STOP    Docker Build
             ↓
        Docker Tag
             ↓
        Docker Login
             ↓
        Docker Push
             ↓
         Docker Hub
             ↓
      Docker Compose
             ↓
         Deployment
```

---

# 24. Security

## Current Security Practices

The project uses Jenkins Credentials for Docker Hub authentication.

Credentials are not stored directly inside the Jenkinsfile.

## Important Production Improvements

For a real production deployment:

- Store secrets in a secret manager
- Use environment variables/secrets
- Avoid hardcoded Flask `SECRET_KEY`
- Use HTTPS
- Restrict access to Jenkins
- Follow least-privilege access
- Rotate credentials
- Avoid running containers with unnecessary privileges

---

# 25. Troubleshooting

## Container Doesn't Start

Check:

```bash
docker ps -a
```

Then:

```bash
docker logs sudoku-app
```

---

## Check Running Containers

```bash
docker ps
```

---

## Check All Containers

```bash
docker ps -a
```

---

## Check Image

```bash
docker images
```

---

## Check Compose

```bash
docker compose ps
```

---

## View Compose Logs

```bash
docker compose logs
```

---

## Port Already in Use

If port 5000 is occupied:

```text
Port 5000
    ↓
Already in use
```

Either stop the existing process/container or map another host port:

```bash
docker run -p 5001:5000 ...
```

Now:

```text
localhost:5001
     ↓
container:5000
```

---

## Docker Hub Login Failure

Check:

- Username
- Access token
- Jenkins credential ID
- Credential type
- Docker Hub permissions

---

## Jenkins Cannot Run Docker

Check:

- Docker CLI installed
- Docker daemon accessible
- Docker socket/configuration
- Jenkins permissions
- Docker Compose plugin availability

---

# 26. Important Commands

## Git

```bash
git status
git add .
git commit -m "message"
git push origin main
git pull
git log
git branch
```

## Docker

```bash
docker build -t sudoku-devops .
docker images
docker run -d -p 5000:5000 --name sudoku-app sudoku-devops
docker ps
docker ps -a
docker logs sudoku-app
docker stop sudoku-app
docker start sudoku-app
docker rm sudoku-app
docker exec -it sudoku-app sh
docker tag
docker push
docker pull
```

## Docker Compose

```bash
docker compose up -d
docker compose down
docker compose ps
docker compose logs
```

## Testing

```bash
python -m pytest
```

---

# 27. Important DevOps Interview Questions

## General DevOps

### Q1. What is DevOps?

> DevOps is a set of practices that improves collaboration and automation between development and operations, enabling faster and more reliable software delivery.

### Q2. Why is automation important in DevOps?

> Automation reduces repetitive manual work, improves consistency, reduces human error, and makes software delivery faster and more repeatable.

### Q3. What is CI?

> Continuous Integration is the practice of frequently integrating code changes and automatically building and testing them.

### Q4. What is CD?

> Continuous Delivery or Continuous Deployment automates the process of preparing or deploying validated software changes.

---

# 28. Project-Based Interview Questions

## Q1. Explain your project.

> "I built a Python Flask Sudoku application and used it as a practical DevOps project. I implemented automated testing with Pytest, containerized the application using Docker and Gunicorn, and created a Jenkins CI/CD pipeline. Jenkins checks out the code from GitHub, runs tests, builds a versioned Docker image, pushes it to Docker Hub, and deploys it using Docker Compose."

---

## Q2. Why did you use Jenkins?

> "I used Jenkins to automate the CI/CD workflow so that testing, Docker image creation, image publishing, and deployment don't have to be performed manually."

---

## Q3. Why Docker?

> "Docker provides a consistent and isolated runtime environment and packages the application with its required dependencies."

---

## Q4. Why Docker Compose?

> "I used Docker Compose to define and manage the application's deployment configuration in a repeatable way."

---

## Q5. Why Docker Hub?

> "Docker Hub acts as the container registry where Jenkins stores the versioned Docker images so they can be pulled during deployment."

---

## Q6. Why use a Jenkinsfile?

> "The Jenkinsfile allows me to define the CI/CD pipeline as code and store it in Git alongside the application."

---

## Q7. How do you version your Docker images?

> "I use Jenkins' BUILD_NUMBER as the Docker image tag. For example, Jenkins build 16 produces the image tagged as `vivekyadavdocker/sudoku-devops:16`."

---

## Q8. How are Docker Hub credentials handled?

> "They are stored in Jenkins Credentials and injected into the pipeline using `withCredentials`, rather than hardcoding them in the Jenkinsfile."

---

# 29. Common Follow-Up Questions

## Docker

- What is a container?
- What is an image?
- What is a Dockerfile?
- What is Docker Compose?
- What is a Docker registry?
- Docker Hub vs Docker?
- What is a Docker volume?
- What is Docker networking?
- What is port mapping?
- What is a Docker layer?
- What is Docker build context?

## Jenkins

- What is a Jenkins pipeline?
- What is a Jenkins agent?
- What is a Jenkins controller?
- What is a Jenkinsfile?
- What is Pipeline as Code?
- What are Jenkins credentials?
- What is `BUILD_NUMBER`?
- What happens when a stage fails?
- How do you trigger Jenkins automatically?
- How do you secure Jenkins?

## Git

- Git vs GitHub?
- What is branching?
- What is merging?
- What is a pull request?
- What is `.gitignore`?
- What is `HEAD`?
- What is a commit?
- What is `git reset`?
- What is `git revert`?

## CI/CD

- CI vs CD?
- Continuous Delivery vs Continuous Deployment?
- Why test before deployment?
- What is a pipeline?
- What is a build artifact?
- What is a quality gate?
- How would you implement rollback?

---

# 30. Final Interview Checklist

Before attending an interview, make sure you can explain these without looking at notes.

## Git

- [ ] Git
- [ ] GitHub
- [ ] Repository
- [ ] Branch
- [ ] Commit
- [ ] Push
- [ ] Pull
- [ ] `.gitignore`

## Docker

- [ ] Docker
- [ ] Image
- [ ] Container
- [ ] Dockerfile
- [ ] Docker build
- [ ] Docker run
- [ ] Port mapping
- [ ] `.dockerignore`
- [ ] Docker logs
- [ ] Docker registry

## Docker Compose

- [ ] compose.yaml
- [ ] Services
- [ ] `docker compose up`
- [ ] `docker compose down`
- [ ] Environment variables

## Jenkins

- [ ] Jenkins
- [ ] Pipeline
- [ ] Jenkinsfile
- [ ] Pipeline as Code
- [ ] Stages
- [ ] Agents
- [ ] Credentials
- [ ] BUILD_NUMBER

## CI/CD

- [ ] Continuous Integration
- [ ] Continuous Delivery
- [ ] Continuous Deployment
- [ ] Automated testing
- [ ] Automated build
- [ ] Image publishing
- [ ] Automated deployment

## Security

- [ ] Jenkins Credentials
- [ ] Docker Hub token
- [ ] Secret management
- [ ] No hardcoded passwords
- [ ] Least privilege

## Troubleshooting

- [ ] `docker ps`
- [ ] `docker logs`
- [ ] `docker compose ps`
- [ ] `docker compose logs`
- [ ] Jenkins console output
- [ ] Port conflicts
- [ ] Docker Hub authentication
- [ ] Docker daemon issues

---

# 🎯 Most Important Diagram

Memorize this:

```text
                  GIT
                   │
                   ▼
                GITHUB
                   │
                Git Push
                   │
                   ▼
                JENKINS
                   │
             ┌─────┴─────┐
             │           │
             ▼           ▼
          CHECKOUT      TEST
                         │
                       PASS
                         │
                         ▼
                    DOCKER BUILD
                         │
                         ▼
                    DOCKER TAG
                         │
                         ▼
                  DOCKER HUB PUSH
                         │
                         ▼
                   DOCKER HUB
                         │
                         ▼
                 DOCKER COMPOSE
                         │
                         ▼
                    DEPLOYMENT
```

---

# 🏆 Final Project Statement

The key DevOps concepts demonstrated by this project are:

```text
Git
 ↓
Version Control

GitHub
 ↓
Source Code Repository

Jenkins
 ↓
CI/CD Automation

Pytest
 ↓
Automated Testing

Docker
 ↓
Containerization

Gunicorn
 ↓
Production WSGI Server

Docker Hub
 ↓
Container Registry

Docker Compose
 ↓
Deployment

Jenkins Credentials
 ↓
Secret Management

BUILD_NUMBER
 ↓
Image Versioning
```

## Final Mental Model

```text
CODE
  ↓
COMMIT
  ↓
PUSH
  ↓
JENKINS
  ↓
TEST
  ↓
BUILD
  ↓
PACKAGE
  ↓
PUBLISH
  ↓
DEPLOY
  ↓
RUN
```

This is the core DevOps story of the Sudoku DevOps project.

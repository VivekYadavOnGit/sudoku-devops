pipeline {
    agent none

    stages {

        stage('Checkout') {
            agent any

            steps {
                echo 'Checking out source code...'

                git branch: 'main',
                    url: 'https://github.com/VivekYadavOnGit/sudoku-devops.git'
            }
        }

        stage('Run Tests') {
            agent {
                docker {
                    image 'python:3.14-slim'
                }
            }

            steps {
                echo 'Installing dependencies...'

                sh 'python -m pip install -r requirements-dev.txt'

                echo 'Running tests...'

                sh 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            agent any

            steps {
                echo 'Building Docker image...'

                sh 'docker build -t sudoku-devops:${BUILD_NUMBER} .'

                sh 'docker tag sudoku-devops:${BUILD_NUMBER} vivekyadavdocker/sudoku-devops:${BUILD_NUMBER}'
            }
        }

        stage('Push to Docker Hub') {
            agent any

            steps {
                echo 'Pushing Docker image to Docker Hub...'

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USERNAME',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin
                        docker push vivekyadavdocker/sudoku-devops:${BUILD_NUMBER}
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy') {
            agent any

            steps {
                echo 'Deploying Sudoku application...'

                sh '''
                    docker stop sudoku-app || true
                    docker rm sudoku-app || true

                    docker run -d \
                        --name sudoku-app \
                        -p 5000:5000 \
                        sudoku-devops:${BUILD_NUMBER}
                '''
            }
        }
    }
}
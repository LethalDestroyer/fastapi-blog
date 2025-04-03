pipeline {
    agent any

    environment {
        IMAGE = "devopsdestroyer/fastapi-blog"
        TAG = "latest"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repo...'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Pushing image...'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to cluster...'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}

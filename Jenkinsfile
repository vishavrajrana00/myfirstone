pipeline {
  agent any

  stages {
    stage('Git Clone') {
      steps {
        git 'https://github.com/vishavrajrana00/myfirstone.git'
      }
    }
    
    stage('Build Image') {
      steps {
        script {
          sh '''
            eval $(minikube -p minikube docker-env)
            docker build -t test-backend ./backend
            docker build -t test-frontend ./frontend
          '''
        }
      }
    }
    
    stage('Push to Registry') {
      steps {
        script {
          // You can skip or configure this if you want to push images to DockerHub or another registry
          echo "Skipping push to registry - Using Minikube local Docker"
        }
      }
    }
    
    stage('Update Deployment') {
      steps {
        script {
          sh '''
            kubectl set image deployment/frontend frontend=test-frontend
            kubectl set image deployment/backend backend=test-backend
          '''
        }
      }
    }
  }
}

pipeline{
    agent any
    environment {
    KUBECONFIG = '/tmp/jenkins-kubeconfig'
    }
    stages{
        stage('Remove previous image'){
            steps{
                sh 'docker rmi flask-app'
            }
        }
        stage('Remove previous deployment & service'){
            steps{
                sh 'kubectl delete deployment flask-deployment'
                sh 'kubectl delete service flask-service'
            }
        }
        stage('Pull') {
            steps{
                 git "https://github.com/Bardy3272/K8-Project"
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Run Deployment & Service') {
            steps {
                sh 'kubectl apply -f flask-deployment.yaml'
                sh 'kubectl apply -f flask-service.yaml'
            }
        }
    }
}

pipeline {
    agent none
    environment {
    registry = "sw9719/pytest"
    registryCredential = "dockerhub"
    }
    stages {
        stage('Build and Test') {
            agent { dockerfile true }
            steps {
                sh 'pytest'
            }
        }
        stage('Push image') {
            agent none
            steps {
               script {
                 dockerImage = docker.build registry
                 docker.withRegistry( '', registryCredential ) {
                   dockerImage.push()
                 }
               }
             }
         }
     }    
}

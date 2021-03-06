pipeline {
    agent none
    environment {
    registry = "sw9719/pytest"
    registryCredential = "dockerhub"
    CLUSTER = credentials('clustercreds')
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
        stage('Deploy') {
            agent any
            steps {
               sh '''
                  oc login -u $CLUSTER_USR -p $CLUSTER_PSW https://api.ayaka.ocp4.link:6443 --insecure-skip-tls-verify
                  helm upgrade pytest myapp
                  oc rollout restart deployment $(grep -i fullnameOverride myapp/values.yaml | awk '{print $2}'| tr -d \\")
                  oc logout
                  '''
            }
        }
     }    
}

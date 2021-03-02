pipeline {
    agent any
    environment {
        registry = "karolinasura/new"
        registryCredentials = 'AUTHOR'
        dockerImage = ''
    }
    stages{
        stage('Test'){
            steps{
                sh './jenkins_scripts/test.sh'
            }
        }
        stage('Build'){
            steps{
                script{
                    git "https://github.com/SuraKarolina/QA-Project-2.git"
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Push'){
            steps{
                script{
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Clean up'){
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
        stage('Configure ansible'){
            steps {
                sh './jenkins_scripts/configure.sh'
            }
        }
        stage('Deploy'){
            steps{
                sh './jenkins_scripts/deploy.sh'
            }
        }                   
    }
}
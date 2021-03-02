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
                sh './jenkins_scripts/build.sh'
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
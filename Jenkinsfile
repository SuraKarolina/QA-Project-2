pipeline {
    agent any
    stages{
        stage('Test'){
            steps{
                sh './jenkins_scripts/test.sh'
            }
        }
        stage('Build'){
            steps{
                node {
                    checkout scm
                    def customImage = docker.build("[karolinasura]/service1")
                    customImage.push()

                    customImage.push('latest')
                }
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
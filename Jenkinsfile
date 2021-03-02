pipeline {
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
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
                    if (env.rollback == 'false'){
                        image = docker.build("[karolinasura]/service1")
                    }
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
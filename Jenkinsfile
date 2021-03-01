pipeline {
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        AUTHOR = credentials("AUTHOR")
        app_version=1
        rollback='false'
    }
    stages{
        stage('Test'){
            steps{
                sh './jenkins_scripts/test.sh'
            }
        }
        stage('Build'){
            steps{
                image = docker.build("[karolinasura]/service1")
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
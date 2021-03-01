pipeline {
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        app_version=1
        rollback='true'
    } 
    stages{
        stage('Test'){
            steps{
                sh './jenkins_scripts/test.sh'
            }
        }
        stage('Configure ansible'){
            steps {
                sh './jenkins_scripts/configure.sh'
            }
        }
        stage("Build"){
            steps{
                script {
                    sh './jenkins_scripts/build.sh'
                }  
            }
        }
        stage('Deploy'){
            steps{
                sh './jenkins_scripts/deploy.sh'
            }
        }                   
    }
}
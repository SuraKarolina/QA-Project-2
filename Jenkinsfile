pipeline {
    agent any 
    stages{
        stage('Configure'){
            steps{
                sh './jenkins_scripts/configure.sh'
            }
        }
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
        stage('Deploy'){
            steps{
                sh './jenkins_scripts/deploy.sh'
            }
        }                   
    }
}

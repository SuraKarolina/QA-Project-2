pipeline {
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        app_version=1
        rollback='true'
    } 
    stages{
        stage('Configure ansible'){
            steps {
                sh './jenkins_scripts/configure.sh'
            }
        }
        stage('Test'){
            steps{
                if (env.rollback == 'false'){
                    sh './jenkins_scripts/test.sh'
                }
            }
        }
        stage("Build"){
            steps{
                script {
                    if (env.rollback == 'false'){
                        sh './jenkins_scripts/build.sh'
                    }
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
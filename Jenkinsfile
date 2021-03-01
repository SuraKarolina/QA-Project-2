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
        stage("Build"){
            steps{
                    sh "docker rmi -f \$(docker images -qa) || true"
                    sh "docker-compose build --parallel --build-arg APP_VERSION=${app_version} && docker-compose push"
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
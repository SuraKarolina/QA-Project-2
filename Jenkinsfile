pipeline {
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        AUTHOR = credentials("AUTHOR")
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
                sh "docker-compose build --parallel --build-arg APP_VERSION=${app_version} && docker-compose push"
                sh "docker system prune -af"
                sh "bash jenkins/build_images.sh"
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
pipeline {
    agent any
    stages{
        stage('Test'){
            steps{
                sh './jenkins_scripts/test.sh'
            }
        }
        stage("Build"){
            steps{
                sh "docker-compose build"
                sh "docker.withRegistry('<your docker registry>', 'docker-private-credentials') {
                    app.push("${app_version}")
                    app.push("latest")"
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
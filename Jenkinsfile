pipeline {
    agent any 
    stages{
        stage('Configure'){
            steps{
            mkdir -p ~/.local/bin
            echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
            source ~/.bashrc
            pip3 install --user ansible
            ansible-playbook -i inventory playbook.yaml 
            }
        }
        stage('Test'){
            steps{
            # test servcie1
            cd ./service1
            pip3 install -r requirements.txt
            python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml 
            cd ..

            # test servcie2
            cd ./service2
            python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
            cd ..

            # test servcie3
            cd ./service3
            python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
            cd ..

            # test servcie4
            cd ./service4
            python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
            cd ..
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

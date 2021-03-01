scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@manager-swarm:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@manager-swarm << EOF
    export DATABASE_URI=${DATABASE_URI}
    export AUTHOR=${AUTHOR}
    export DB_PASSWORD=${DB_PASSWORD}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yml financial-report-generator-stack
EOF
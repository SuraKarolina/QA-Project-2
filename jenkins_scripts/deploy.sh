#!/bin/bash
ssh manager << EOF
scp /home/karolina_sura/QA-Project-2/docker-compose.yaml /home/jenkins/
export SECRET_KEY=${SC_KEY} 
export DATABASE_URI=${DB_URI} 
docker stack deploy --compose-file docker-compose.yaml
EOF
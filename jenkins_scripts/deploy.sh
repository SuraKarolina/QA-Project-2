#!/bin/bash
ssh manager << EOF
scp /home/jason/SFIA_Project_Week_9/docker-compose.yaml /home/jenkins/
export SECRET_KEY=${SC_KEY} 
export DATABASE_URI=${DB_URI} 
docker stack deploy --compose-file docker-compose.yaml sfia2
EOF
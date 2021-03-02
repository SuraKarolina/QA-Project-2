#!/bin/bash
pwd
sudo chmod 666 /var/run/docker.sock

dockerImage = docker.build registry + ":$BUILD_NUMBER"
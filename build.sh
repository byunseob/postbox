#!/bin/bash

DOCKER_VERSION=`cat DOCKER_VERSION`
APP_NAME=postbox
REGISTRY=byunseob

docker build -t ${REGISTRY}/${APP_NAME}:latest .
docker tag ${REGISTRY}/${APP_NAME}:latest ${REGISTRY}/${APP_NAME}:${DOCKER_VERSION}
docker push ${REGISTRY}/${APP_NAME}:latest
docker push ${REGISTRY}/${APP_NAME}:${DOCKER_VERSION}

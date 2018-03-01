#!/usr/bin/env bash

image_name="$1"

echo "Autenticándose"
docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASS";
echo "Subiendo imágen"
docker push "$image_name"
echo "Subida"

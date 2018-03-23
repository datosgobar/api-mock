#!/bin/bash

set -e;

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

TAG="$1"
ENVIRONMENT="$2"

"$DIR/upload_image.sh" "datosgobar/api-mock:$TAG"

if [ -n "$ENVIRONMENT" ]; then
    echo "Corriendo Continuous Deployment en $ENVIRONMENT";
    "$DIR/deploy/run_deploy.sh" "$ENVIRONMENT"
else
    echo "Sin ambiente para Continuous Delivery"
fi


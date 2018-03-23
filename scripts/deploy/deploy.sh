#!/bin/bash

set -e;

echo "Agregando clave SSH"
eval "$(ssh-agent -s)"
ssh-add deploy-api@travis-ci.org

# Nota: Las variables no definidas aqui deben ser seteadas en ./variables.sh

# TODO: Mejorar este script.
echo "Actualizando el deployment..."
ssh $DEPLOY_TARGET_USERNAME@$DEPLOY_TARGET_IP -p$DEPLOY_TARGET_SSH_PORT "\
    cd ~/apimock-dev/api-mock/deploy && \
    git pull"

echo "Ejecutando comando de instalación..."
ssh $DEPLOY_TARGET_USERNAME@$DEPLOY_TARGET_IP -p$DEPLOY_TARGET_SSH_PORT "\
    source ~/apimock-dev/venv/bin/activate && \
    ansible-playbook -i inventories/$DEPLOY_ENVIRONMENT/hosts --extra-vars='checkout_branch=$DEPLOY_REVISION' --vault-password-file $DEPLOY_TARGET_VAULT_PASS_FILE site.yml"

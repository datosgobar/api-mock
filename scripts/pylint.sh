#!/usr/bin/env bash
set -e
DIR=$(dirname "$0")
cd ${DIR}/..

echo "Running pylint"
pylint --load-plugins pylint_django api_mock/
echo "pylint OK :)"



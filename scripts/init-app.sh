#!/bin/bash

set -e

cd ..

docker build . -t "user-app"

docker-compose up
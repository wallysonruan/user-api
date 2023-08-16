#!/bin/bash

set -e

cd ..

docker build . -t "teste"

docker-compose up
#!/bin/bash

set -e

docker build ../ -t "user-app"

docker-compose up
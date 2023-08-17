#!/bin/bash

# This script assumes that:
#
# 1. There's a Postgres container running already.
#
# Docker command if not:
#
# docker run --name user_psql -e POSTGRES_PASSWORD=user
# -e POSTGRES_USER=user -p 5432:5432 -d postgres
#
# 2. You've a virtual environment running.
#
# If not, open the terminal, go to the simple_user_project folder, and run:
# python3 -m venv .
#
# Then, run the command below:
# source venv/bin/activate
#

set -e

# Runs a Postgres database.
docker run --name user_psql -e POSTGRES_PASSWORD=user -e POSTGRES_USER=user -p 5432:5432 -d postgres

# Install all the dependencies declared in the requirements.txt file
pip install -r "environment_configs/requirements.txt"

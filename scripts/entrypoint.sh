#!/bin/bash

# Give the database container time
sleep 3

# Apply migrations to the database
alembic upgrade head

# Starts web server
uvicorn main:app --host "0.0.0.0" --port 80
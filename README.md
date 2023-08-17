# Web API Application using Python, FastAPI, SQLAlchemy, and Docker

This repository contains a simple Web API application developed using Python, FastAPI, SQLAlchemy, databases, Postgres, Docker, and Bash. The application provides endpoints for interacting with a database and demonstrates how to set up a development environment, containerize the application, and use various tools for building a robust API.

## Features

- Utilizes FastAPI to create a modern and efficient web API.
- Integrates SQLAlchemy and databases libraries for database interactions.
- Uses Postgres as the database backend for data storage.
- Containerized using Docker for easy deployment and scalability.
- Includes Bash scripts to automate deployment tasks.

## Development Environment Setup

To set up the development environment for this project, you'll need the following tools:

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) for containerization and easy development environment setup.
- [Python 3>](https://www.python.org/) for coding the application logic.
- [Pip](https://pypi.org/project/pip/) to manage the dependencies.
- [Postgres](https://www.postgresql.org/) as the chosen database backend.
- [Bash](https://www.gnu.org/software/bash/) for running scripts and automation.


## Getting Started

1. Clone the repository: `git clone https://github.com/wallysonruan/user-api.git`
2. Go to the user-api/ folder.

### Local
   1. Run `python3 -m venv .`, to start a virtual environment.
   2. Go to the scripts/ folder.
   3. Run `bash bootstrap.sh`, to start a Postgres database in a container (you can not have any other process 
   running on the port 5432), and install all the dependencies needed.
   4. Run `uvicorn main:app --reload` – make sure you are on the app home folder.
   5. Access the API endpoints via a web browser or API client, you can check the `http://localhost:8000/docs`
   to see all endpoints.

### Container
   1. Go to the scripts/ folder.
   2. Run `bash init-app.sh`, to start the Postgres database (you can not have any other process 
   running on the port 5432), and the application in containers.
   3. Access the API endpoints via a web browser or API client, you can check the `http://localhost:8000/docs`
   to see all endpoints.

## Roadmap

- [ ] Implement unit and integration tests using Pytest to ensure code quality and reliability.
- [ ] Enhance security by implementing JSON Web Tokens (JWT) authentication for selected endpoints.

## Contributing

Contributions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a pull request.

FROM python:slim

WORKDIR /usr/src/app
COPY .. ./

# Activate flag to use the database DNS instead of 'localhost', check env.py
ENV USER_ENV=PROD

# Install dependencies
RUN pip install --no-cache-dir -r environment_configs/requirements.txt

# Starts the web server
ENTRYPOINT ["bash", "scripts/entrypoint.sh"]

FROM python:slim

WORKDIR /usr/src/app
COPY . ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Starts the web server
ENTRYPOINT ["bash", "scripts/entrypoint.sh"]

#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/denma-group/website-backend-django.git'

# Directory we're going the story the project in the server.
PROJECT_BASE_PATH='/usr/local/apps/denma_api'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic. Command collectstatic will gather all static files for all of the files in the
# project into one directory. This is for the Django Admin browsable API.
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_denma_api.conf /etc/supervisor/conf.d/denma_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart denma_api

# Configure nginx
cp $PROJECT_BASE_PATH/deploy/nginx_denma_api.conf /etc/nginx/sites-available/denma_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/denma_api.conf /etc/nginx/sites-enabled/denma_api.conf
systemctl restart nginx.service

echo "DONE! :)"

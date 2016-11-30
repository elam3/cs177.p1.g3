# Installation
Recommended: `Python 3.5.2`, `Django 1.10`

### Setup a Virutal Environment

> Install virtualenv if needed, i.e. `sudo apt-get install virtualenv`

virtualenv --python=$(which python3) ~/venvs/myenv
source ~/venv/myenv/bin/activate
pip install --requirements pip.reqs

### Run the server
python manage.py runserver
open in browser: localhost:8000/1

### Sharing the app
Install ngrok
~/Downloads/ngrok http localhost:8000
Share the url

### Using the app
Student view: localhost:8000/1
Admin view: localhost:8000/1/results

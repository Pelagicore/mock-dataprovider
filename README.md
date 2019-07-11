# Mock Data Provider

A django based web service to provide music, movie, contacts and other data in JSON format.

## Install

If you want to, you can setup a virtual environment for Python. This helps separating the installations made using `pip` from the rest of the system.

Ensure you point the virtual environment to a Python3 instance.

    virtualenv p /usr/local/bin/python3 venv
    source venv/bin/activate
    
To exit the virtual environment, simply type

    deactivate

The following steps are compulsory regardless if you choose to work in a virtual environment or not.

To install prerequisites web server

    pip install -r requirements.txt

## Run

    cd src/
    ./manage.py migrate
    ./manage.py runserver

The server is available under http://localhost:8000/

The different web-services under

    http://localhost:8000/api/music/
    http://localhost:8000/api/movies/
    http://localhost:8000/api/contacts/
    http://localhost:8000/api/photos/

## To Scan for Data

The media data must reside in ~/media

    ~/media/music
    ~/media/movies
    ~/media/photos

To scan for media use:

    ./manage.py scanmovies
    ./manage.py scanmusic
    ./manage.py scancontacts
    ./manage.py scanphotos

or use the help for manage.py

    ./manage.py help

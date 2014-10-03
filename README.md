Data Provider
=============

A django based web service to provide music, movie, contacts and other data in JSON format.

Install
-------

For the web server

    pip install django
    pip install djangorestframework
    pip install django-filter
    pip install django-grappelli
    pip install django-filebrowser

To enable music/video scanning

    pip install mutagen

Run
---

    cd src/
    ./manage.py syncdb
    ./manage.py runserver

The server is available under http://localhost:8000

The different web-services under

    http://localhost:8000/music
    http://localhost:8000/movies
    http://localhost:8000/contacts
    http://localhost:8000/photos

To Scan for Data
----------------

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



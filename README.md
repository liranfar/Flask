## What is Flask?

> Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!

## Usage

    $ git clone https://github.com/liranfar/Flask.git flask

    $ cd flask

    $ sudo apt-get install  pip virtualenv virtualenvwrapper

    $ mkvirtualenv flask

    $ pip install -r requirements.txt

    $ export FLASK_CONFIGURATION='development'
    
    $ export DATABASE_URL='<your_connection_uri>'
    
    $ python manage.py upgrade
    
    $ python seed.py
    
    $ python manage.py runserver    
    
for de/activating virtual environment:

    $ workon flask

    $ deactivate

## Front-End
    $ sudo npm install -g gulp bower
    
    $ npm install
    
    $ bower install
    
    $ gulp
    
   
* Install & enable [LiveReload](https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei) Chrome extension 
* Make sure to disable browser caching in developer tools (checkbox)

## Resources

1. [Official Documentation](http://flask.pocoo.org/)
2. https://exploreflask.com/en/latest/
3. https://www.fullstackpython.com/
4. https://pythonhosted.org/Flask-Security/
5. http://flask-sqlalchemy.pocoo.org/
6. [RealPython - Flask](https://realpython.com/blog/python/introduction-to-flask-part-1-setting-up-a-static-site/)
7. https://damyanon.net/post/flask-series-structure/
8. https://flask-script.readthedocs.io/en/latest/
9. [React](https://reactjs.org/)
9. [Gulp](https://gulpjs.com/)
ping
====

Application for managing Ping Pong Matches

# Instalation

Distribute should take care of most of the setup for you.
Provided you already have a virtualenv do:

    $ python setup.py develop

Now you can run `manage`, which is just a shortcut to the project's manage.py
script:

    $ manage syncdb

It'll probably require you to set a `DATABASE_URL` environment variable

    $ export DATABASE_URL=sqlite:///partidos.db


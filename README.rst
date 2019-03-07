============
Deck Crafter
============

Many people play Collectible Card Games (or CCGs), but it can be kind
of a pain to build a deck by rummaging around in a physical collection
of cards, and friends who want to play will have to have their own
cards or wait until they have access to yours.  Deck Crafter makes it
possible to build decks from a virtual collection of cards, which can
then be quickly realized as a physical deck when getting together for
a gaming session.


Requirements
------------

- Python 3.5+
- Django 2.0+
- PostgreSQL


Installation
------------

Use pip to install deck-crafter from Github
::

   pip install git+https://github.com/jbradberry/deck-crafter.git


or from your local development copy
::

   pip install -e deck-crafter/


Configuration
-------------

Add deck_crafter to the ``INSTALLED_APPS`` list in your settings file.
::

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Added.
        'deck_crafter',
    ]

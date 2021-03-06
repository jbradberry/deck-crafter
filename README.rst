============
Deck Crafter
============

.. image:: https://travis-ci.com/jbradberry/deck-crafter.svg?branch=master
    :target: https://travis-ci.com/jbradberry/deck-crafter

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
- sorl-thumbnail


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
        'sorl.thumbnail',
    ]


Also be sure to include ``deck_crafter.urls`` in your root urlconf.

Example::

    from django.urls import include, url, reverse_lazy
    from django.views.generic import RedirectView

    urlpatterns = [
        url(r'^$', RedirectView.as_view(url=reverse_lazy('game_list'), permanent=False)),
        url(r'^', include('deck_crafter.urls')),
        url(r'^admin/', include('admin.site.urls')),
        url(r'^accounts/', include('django.contrib.auth.urls'),
    ]

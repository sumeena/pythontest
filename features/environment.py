# -*- coding: utf-8 -*-
"""environment -- environmental setup for Django+Behave+Mechanize
basic solution: https://github.com/nathforge/django-mechanize/

"""
import os
from splinter import Browser

os.environ['DJANGO_SETTINGS_MODULE'] = 'gongaloo.settings'


def before_all(context):
    from django.conf import settings


    from django.test import utils
    utils.setup_test_environment()


    # required because we are using south
    from south.management.commands import patch_for_test_db_setup
    patch_for_test_db_setup()

    ### Set up the WSGI intercept "port".
    import wsgi_intercept
    from django.core.handlers.wsgi import WSGIHandler
    host = context.host = 'localhost'
    port = context.port = getattr(settings, 'TESTING_MECHANIZE_INTERCEPT_PORT', 17681)

    # NOTE: Nothing is actually listening on this port. wsgi_intercept
    # monkeypatches the networking internals to use a fake socket when
    # connecting to this port.
    wsgi_intercept.add_wsgi_intercept(host, port, WSGIHandler)

    import urllib.parse as urlparse
    def browser_url(url):
        """Create a URL for the virtual WSGI server.

        e.g context.browser_url('/'), context.browser_url(reverse('my_view'))
        """
        return urlparse.urljoin('http://%s:%d/' % (host, port), url)

    context.browser_url = browser_url

    ### BeautifulSoup is handy to have nearby. (Substitute lxml or html5lib as you see fit)
    from bs4 import BeautifulSoup
    def parse_soup():
        """Use BeautifulSoup to parse the current response and return the DOM tree.
        """
        r = context.browser.response()
        html = r.read()
        r.seek(0)
        return BeautifulSoup(html)

    context.parse_soup = parse_soup


def before_scenario(context, scenario):
    # Set up the scenario test environment

    # We must set up and tear down the entire database between
    # scenarios. We can't just use db transactions, as Django's
    # TestClient does, if we're doing full-stack tests with Mechanize,
    # because Django closes the db connection after finishing the HTTP
    # response.
    from django.db import connection
    connection.creation.create_test_db(verbosity=1, autoclobber=True)

    ### Set up the Mechanize browser.

    # MAGIC: All requests made by this monkeypatched browser to the magic
    # host and port will be intercepted by wsgi_intercept via a
    # fake socket and routed to Django's WSGI interface.
    browser = context.browser = Browser()
    #browser.set_handle_robots(False)


def after_scenario(context, scenario):
    # Tear down the scenario test environment.
    from django.db import connection
    #connection.creation.destroy_test_db('gongaloo', verbosity=1)
    # Bob's your uncle.


def after_all(context):
    from django.test import utils
    utils.teardown_test_environment()
    context.browser.quit()
    context.browser = None

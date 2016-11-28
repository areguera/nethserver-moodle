=================
nethserver-moodle
=================

This package provides NethServer templates and events needed to
integrate Moodle learning platform in NethServer.

Installation
============

When installed, the package does the following:

* install `moodle` package from EPEL repository
* create ``moodle`` mysql database
* create default database credentials: user `moodle` and password stored in ``/var/lib/nethserver/secrets/moodle``
* create NethServer applications entry to access Moodle web interface

Configuration
=============

Once installed, `moodle` needs to be configured in order to used.  The
configuration process takes place the first time you access Moodle's
web interface and consists on the following straightforward actions:

* System verification. It should be pass all without any problem
  except two warnings checks about `php-soap` and `opcache` which can
  be ignored by pressing the continue button.

* Database population. It should be pass all without any problem.
  When done, press the continue button.

* Administrator account creation. Here you need to enter the
  administrator profile (including password and e-mail). When done,
  press Update Profile button. It will take a moment and will take you
  to Moodle learning platform admin interface.

Related configuration are stored inside the ``configuration`` db,
under the ``moodle`` key but it is empty right now. No properties have
been defined either.

Authentication
==============

Once configured, `moodle` uses an internal account provider to handle
user information. To change the account provider you need to access
Moodle's web interface using the admin account and search for "Manage
authentication" inside the administration block. Then activate or
deactivate the authentication plugin you want to use or not. Finally
it is necessary to adjusts the authentication plugin settings in order
to make it working appropriately.

Backup
======

The Moodle backup includes the configuration file and all data: 

* /var/www/moodle/data/

The database is automatically saved by ``nethserver-mysql``.


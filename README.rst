=================
nethserver-moodle
=================

This package can be installed before or after any user provider like
nethserver-dc and nethserver-directory.

If nethserver-dc or nethserver-directory are installed, the
nethserver-moodle-save event will automatically enable all local
users.

The package does the following:

* create ``moodle`` mysql database
* create default database credentials: user `moodle` and password stored in ``/var/lib/nethserver/secrets/moodle``

The configuration is stored inside the ``configuration`` db, under the
``moodle`` key.

Properties: None.

Backup
======

The Moodle backup includes the configuration file and all data: 

* /var/www/moodle/web/config.php
* /var/www/moodle/data/

The database is automatically saved by ``nethserver-mysql``.


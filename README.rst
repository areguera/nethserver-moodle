=================
nethserver-moodle
=================

This package provides NethServer templates and events needed to
integrate Moodle learning platform in NethServer.

Installation
============

When installed, the package does the following:

* Install `moodle` package from EPEL repository

* Install `moodle` package dependencies (e.g., `php-soap`,
  `php-pecl-zendopcache`, `php-ldap`) not considered by `moodle`
  package itself.

* Create ``moodle`` mysql database

* Create default database credentials: user `moodle` and password
  stored in ``/var/lib/nethserver/secrets/moodle``

* Create Moodle entry in NethServer applications

* Create `moodle` key in NethServer configuration database. Under this
  key you'll find both `host` and `path` properties

Configuration
=============

Once installed, `moodle` needs to be configured in order to be used.
The configuration process takes place the first time you access
Moodle's web interface and it consists on the following
straightforward actions:

* *System verification* -- It should pass all without any warning.
  When done, press the continue button.

* *Database population* -- It should pass all without any problem.  When
  done, press the continue button.

* *Administrator account creation* -- Here you need to enter the
  administrator profile (including password and e-mail). When done,
  press Update Profile button. It will take a moment and the Moodle
  learning platform administrator interface will be shown for you to
  complete setting the learning environment.

Once `moodle` has been configured through the web interface, you can
use NethServer database configuration tool to customize the URL used
to reach Moodle web application either to use *Alias* or a *Virtual
Host*.

* *Alias* -- This is the default implemented solution, and takes place
  when the value of *host* property is empty and the value of *path*
  property is non-empty and it doesn't begin with dot or slash in
  which case the value introduced will be replaced by `moodle`. To
  implement this solution run the following commands:

    db configuration setprop moodle host "";
    db configuration setprop moodle path moodle;
    signal-event nethserver-moodle-update;

* *Virtual Host* -- This solution takes place when the value of *host*
  property is non-empty and the value of  *path* property is empty. In
  this case, the web server is reconfigured to use a customized value
  of property *host* as reference to build a virtualhost-like
  configuration and serve Moodle that way. To implement this solution
  run the following commands:

    db configuration setprop moodle host "vhost.your.domain";
    db configuration setprop moodle path "";
    signal-event nethserver-moodle-update;

  *CAUTION:* In order for this solution to work, the
  `vhost.your.domain` must have a valid entry in the system's hosts
  database so to reach the server IP correctly.

Presently, the properties available in the `moodle` key have the
following meaning:

* *host* -- This option sets the host name par of the URL used to
  access Moodle. By default it uses the same host name of the HTTP
  request. You can change the value of this property to fit your
  needs. In that case be aware of the CAUTION admonition above.

* *path* -- This option sets the path part of the URL used to access
  Moodle. By default the value of this property is set to `moodle`.
  You can change the value of this property to fit your needs. In that
  case be aware it must not begin with dot (.) or slash (/) because
  the entire value will be ignored and replaced with the string
  `moodle`.

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


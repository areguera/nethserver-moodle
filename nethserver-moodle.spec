Name: nethserver-moodle
Summary: Moodle integration in NethServer
Version: 0.0.6
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

Requires: moodle >= 3.1.2
# Moodle dependencies (not included in moodle spec).
Requires: php-soap, php-pecl-zendopcache, php-ldap
# NethServer dependencies.
Requires: nethserver-httpd, nethserver-mysql

%description
This package provides NethServer templates and actions needed to
integrate Moodle learning platform in NethServer.


%prep
%setup


%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root/etc/e-smith/templates/var/www/moodle/web/config.php/; ln -s /etc/e-smith/templates-default/template-begin-php template-begin)
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist


%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING README.rst
%dir %{_nseventsdir}/%{name}-update


%changelog
* Mon Nov 28 2016 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.6-1
- Add a property to restrict to the LAN if wanted
- Add moodle dependencies not included in moodle spec itself

* Sun Nov 27 2016 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.5-1
- Remove /var/lib/nethserver/moodle directory
- Remove sudoers.d reference from package spec
- Remove 90_nethserver_moodle from sudoers.d
- Remove config.php from backup-data.d/moodle.include
- Automate password setting in config.php template

* Sun Nov 27 2016 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.4-1
- Update README.rst
- Consider README.rst a documentation file

* Sat Nov 26 2016 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.3-1
- Fix template header in config.php
- Remove duplicated php opening tag from final config.php file
- Remove ^M characters from config.php file
- Update config.php to use https instead of http as value to wwwroot

* Sat Nov 26 2016 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.2-1
- Fix access control in moodle.conf
- Fix moodle's module class name definition

* Fri Nov 25 2016 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-1
- Initial build.

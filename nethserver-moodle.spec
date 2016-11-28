Name: nethserver-moodle
Summary: Moodle integration in NethServer
Version: 0.0.5
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

Requires: moodle >= 3.1.2
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
mkdir -p %{buildroot}/var/lib/nethserver/moodle
%{genfilelist} %{buildroot} --dir /var/lib/nethserver/moodle 'attr(0755,apache,apache)' > %{name}-%{version}-filelist


%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING README.rst
%dir %{_nseventsdir}/%{name}-update
%config %attr (0440,root,root) %{_sysconfdir}/sudoers.d/90_nethserver_moodle


%changelog
* Sun Nov 27 2016 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.5-1
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

Name: nethserver-moodle
Summary: Moodle integration in NethServer
Version: 0.0.1
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
(cd root; find . -depth -print | cpio -dump %{buildroot})
mkdir -p %{buildroot}/var/lib/nethserver/moodle
%{genfilelist} %{buildroot} --dir /var/lib/nethserver/moodle 'attr(0755,apache,apache)' > %{name}-%{version}-filelist


%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%config %attr (0440,root,root) %{_sysconfdir}/sudoers.d/90_nethserver_moodle


%changelog
* Fri Nov 25 2016 Alain Reguera Delgado <alain.reguera@gmail.com> - 0.0.1-1
- Initial build.

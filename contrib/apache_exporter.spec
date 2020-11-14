%define debug_package %{nil}

Name:		apache-exporter
Version:	0.8.0
Release:	1%{?dist}
Summary:	Exports apache mod_status statistics via HTTP for Prometheus consumption
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/Lusitaniae/apache_exporter
Source0:        https://github.com/Lusitaniae/apache_exporter/releases/download/%{version}/apache_exporter-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd systemd
AutoReqProv:	No

%description

Exports apache mod_status statistics via HTTP for Prometheus consumption

%prep
%setup -q -n apache_exporter-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/sbin
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
mkdir -vp $RPM_BUILD_ROOT/opt/prometheus
install -m 755 apache_exporter $RPM_BUILD_ROOT/usr/sbin/apache_exporter
install -m 755 contrib/apache_exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/apache_exporter.service
install -m 644 contrib/apache_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/apache_exporter

%clean

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/prometheus/ -c "Prometheus Daemons" prometheus
exit 0

%post
chgrp prometheus /var/run/prometheus
chmod 774 /var/run/prometheus
chown prometheus:prometheus /opt/prometheus
chmod 744 /opt/prometheus

%files
%defattr(-,root,root,-)
/usr/sbin/apache_exporter
/usr/lib/systemd/system/apache_exporter.service
%config(noreplace) /etc/sysconfig/apache_exporter
/var/run/prometheus
/opt/prometheus

%changelog
* Sat Nov 14 2020 Tsvetan Gerov <tsvetan@gerov.eu> 0.8.0-1
- Update to 8.0.8

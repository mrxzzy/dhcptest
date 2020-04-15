# git ls-remote https://github.com/mrxzzy/dhcptest.git
%global commit 90951ffd3a5e429c89b7b8cbb678b809494eb4f6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%undefine _disable_source_fetch

Name: dhcptest
Version: 1.0
Release: 1%{?dist}
Summary: installs 'dhcptest' as a nagios plugin for testing a dhcp server
Source0: https://github.com/mrxzzy/dhcptest/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

License: nah

%description
%{summary}

%prep
%autosetup -n dhcptest-%{commit}

%build
dmd dhcptest.d

%install
mkdir -p %{buildroot}/usr/lib64/nagios/plugins/
cp dhcptest %{buildroot}/usr/lib64/nagios/plugins/dhcptest

%files
/usr/lib64/nagios/plugins/dhcptest

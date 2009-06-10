Summary:	A "ping"-like tool for HTTP requests
Name:		httping
Version:	1.3.0
Release:	%mkrel 1
Group:		System/Base
License:	GPL+ and OpenSSL
URL:		http://www.vanheusden.com/httping/
Source0:	http://www.vanheusden.com/httping/httping-%{version}.tgz
# patch from fedora, fixes strndup build error on x86_64 - 10Jun2009
Patch0:		httping-strndup.patch
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
httping is a "ping"-like tool for HTTP requests. Give it a URL and it will show
how long it takes to connect, send a request, and retrieve the reply (only the
headers). It can be used for monitoring or statistical purposes (measuring
latency).

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%serverbuild

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 httping %{buildroot}%{_bindir}/httping
install -m0644 httping.1 %{buildroot}%{_mandir}/man1/httping.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc readme.txt license.txt license.OpenSSL
%{_bindir}/httping
%{_mandir}/man1/httping.1*

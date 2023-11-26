# Work around build system deficiencies
%undefine _debugsource_packages

Summary:	A "ping"-like tool for HTTP requests
Name:		httping
Version:	2.9
Release:	1
Group:		System/Base
License:	GPL-3.0
URL:		http://www.vanheusden.com/httping/
Source0:	https://github.com/folkertvanheusden/HTTPing/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(fftw3)

%description
httping is a "ping"-like tool for HTTP requests. Give it a URL and it will show
how long it takes to connect, send a request, and retrieve the reply (only the
headers). It can be used for monitoring or statistical purposes (measuring
latency).

%prep
%autosetup -p1 -n HTTPing-%{version}
# Looks like autoconf, but isn't
%setup_compile_flags
./configure --prefix=%{_prefix} --with-tfo --with-ncurses --with-openssl --with-fftw3

%build
%make_build

%install
%make_install
%find_lang %{name} --with-man

%files -f %{name}.lang
%doc %{_docdir}/%{name}/README.md
%license %{_docdir}/%{name}/LICENSE
%{_bindir}/httping
%{_mandir}/man1/httping.1*
%lang(nl) %{_mandir}/nl/man1/httping-nl.1*
%lang(ru) %{_mandir}/ru/man1/httping-ru.1*

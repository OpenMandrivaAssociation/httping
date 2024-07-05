# Work around build system deficiencies
%undefine _debugsource_packages

Summary:	A "ping"-like tool for HTTP requests
Name:		httping
Version:	3.6
Release:	1
Group:		System/Base
License:	GPL-3.0
URL:		http://www.vanheusden.com/httping/
Source0:	https://github.com/folkertvanheusden/HTTPing/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(fftw3)
BuildSystem:	cmake

%description
httping is a "ping"-like tool for HTTP requests. Give it a URL and it will show
how long it takes to connect, send a request, and retrieve the reply (only the
headers). It can be used for monitoring or statistical purposes (measuring
latency).

%install
# Not using the default install bits here -- CMakeLists.txt
# doesn't contain install instructions

cd _OMV_rpm_build
mkdir -p %{buildroot}%{_bindir}
mv httping %{buildroot}%{_bindir}/
for i in *.mo; do
	mkdir -p %{buildroot}%{_datadir}/locale/$(basename $i .mo)/LC_MESSAGES
	mv $i %{buildroot}%{_datadir}/locale/$(basename $i .mo)/LC_MESSAGES/httping.mo
done
cd ..

mkdir -p %{buildroot}%{_mandir}/man1
mv httping.1 %{buildroot}%{_mandir}/man1/

for i in httping-*.1; do
	L=$(echo $i |cut -d- -f2 |cut -d. -f1)
	mkdir -p %{buildroot}%{_mandir}/$L/man1/
	mv $i %{buildroot}%{_mandir}/$L/man1/httping.1
done

%find_lang %{name} --with-man

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/httping
%{_mandir}/man1/httping.1*

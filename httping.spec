Summary:	A "ping"-like tool for HTTP requests
Name:		httping
Version:	1.5.4
Release:	1
Group:		System/Base
License:	GPLv2+ 
URL:		http://www.vanheusden.com/httping/
Source0:	http://www.vanheusden.com/httping/httping-%{version}.tgz
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel

%description
httping is a "ping"-like tool for HTTP requests. Give it a URL and it will show
how long it takes to connect, send a request, and retrieve the reply (only the
headers). It can be used for monitoring or statistical purposes (measuring
latency).

%prep

%setup -q

%build
%setup_compile_flags

%make OFLAGS="-D_GNU_SOURCE"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 httping %{buildroot}%{_bindir}/httping
install -m0644 httping.1 %{buildroot}%{_mandir}/man1/httping.1

%files
%defattr(-,root,root,-)
%doc readme.txt license.txt license.OpenSSL
%{_bindir}/httping
%{_mandir}/man1/httping.1*


%changelog
* Thu Sep 20 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.5.4-1
+ Revision: 817179
- update to 1.5.4

* Mon Mar 14 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.4.4-1
+ Revision: 644691
- update to new version 1.4.4

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-3mdv2011.0
+ Revision: 611103
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 1.4.1-2mdv2010.1
+ Revision: 537367
- rebuild

* Fri Feb 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.1-1mdv2010.1
+ Revision: 504430
- update to 1.4.1

* Mon Dec 28 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2010.1
+ Revision: 483171
- use -D_GNU_SOURCE instead of the patch

* Mon Aug 03 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 408487
- update to new version 1.3.1

* Thu Jun 11 2009 Jérôme Brenier <incubusss@mandriva.org> 1.3.0-3mdv2010.0
+ Revision: 385011
- really fix strndup conflict (new patch)
- fix strndup build error (patch from fedora)
- update to new version 1.3.0
- fix license

* Tue Oct 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.9-2mdv2009.1
+ Revision: 297830
- fix spec file error

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.9-1mdv2009.0
+ Revision: 236759
- 1.2.9

* Tue Jul 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-1mdv2009.0
+ Revision: 230564
- 1.2.8

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-1mdv2008.0
+ Revision: 80934
- 1.2.5

* Tue Jul 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdv2008.0
+ Revision: 50959
- Import httping



* Tue Jul 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdv2008.0
- initial Mandriva package

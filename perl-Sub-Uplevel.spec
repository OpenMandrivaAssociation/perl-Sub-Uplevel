%define upstream_name    Sub-Uplevel
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Apparently run a function in a higher stack frame
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
BuildArch:	noarch

%description 
Apparently run a function in a higher stack frame.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std
%__rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%check
make test

%files
%doc Changes
%{perl_vendorlib}/Sub
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-4mdv2012.0
+ Revision: 765665
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-3
+ Revision: 764176
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-2
+ Revision: 667318
- mass rebuild

* Sun Nov 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 468889
- update to 0.22

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.200-1mdv2010.0
+ Revision: 393408
- update to 0.2002
- using %%perl_convert_version
- fixed license field

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.18-2mdv2009.0
+ Revision: 224059
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.1
+ Revision: 104470
- update to new version 0.18

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.0
+ Revision: 63962
- update to new version 0.16


* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2007.0
+ Revision: 84383
- new version

* Tue Nov 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2007.1
+ Revision: 83990
- Import perl-Sub-Uplevel

* Sat Jun 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2007.0
- New version 0.13

* Sun May 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdk
- New release 0.12

* Tue Apr 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdk
- New release 0.10
- better sources URL

* Tue Apr 04 2006 Buchan Milne <bgmilne@mandriva.org> 0.09-4mdk
- Rebuild
- use mkrel

* Sun Jun 12 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-3mdk 
- better url
- spec cleanup
- don't ship useless empty dirs
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.09-2mdk
- fix buildrequires in a backward compatible way

* Fri Jul 09 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.09-1mdk
- 0.95

* Thu Apr 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.08-1mdk
- new version
- rpmbuildupdate aware
- no more explicit dependencies, let spec-helper do its job
- make test


%define module  Sub-Uplevel
%define	name	perl-%{module}
%define version 0.18
%define release %mkrel 1

Summary: 	%{module} module for perl
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sub/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch: 	noarch

%description 
Apparently run a function in a higher stack frame.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%check
%{__make} test

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Sub
%{_mandir}/*/*



%define modname	Sub-Uplevel

Summary:	Apparently run a function in a higher stack frame
Name:		perl-%{modname}
Version:	0.2800
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sub/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP

%description 
Apparently run a function in a higher stack frame.

%prep
%setup -qn %{modname}-%{version}

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
%{_mandir}/man3/*


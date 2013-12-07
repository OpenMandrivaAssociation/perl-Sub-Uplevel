%define modname	Sub-Uplevel
%define modver	0.24

Summary:	Apparently run a function in a higher stack frame
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sub/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP

%description 
Apparently run a function in a higher stack frame.

%prep
%setup -qn %{modname}-%{modver}

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


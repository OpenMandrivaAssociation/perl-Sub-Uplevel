%define upstream_name    Sub-Uplevel
%define upstream_version 0.22

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 4

Summary: 	apparently run a function in a higher stack frame
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description 
Apparently run a function in a higher stack frame.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

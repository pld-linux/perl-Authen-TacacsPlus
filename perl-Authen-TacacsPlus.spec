%include	/usr/lib/rpm/macros.perl
Summary:	Authen::TacacsPlus perl module
Summary(pl):	Modu³ perla Authen::TacacsPlus
Name:		perl-Authen-TacacsPlus
Version:	0.16
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Authen/TacacsPlus-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::TacacsPlus - module for authentication using tacacs+ server.

%description -l pl
Authen::TacacsPlus - modu³ do autentykacji przy pomocy serwera tacacs+.

%prep
%setup -q -n TacacsPlus-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Authen/TacacsPlus.pm
%dir %{perl_sitearch}/auto/Authen/TacacsPlus
%attr(755,root,root) %{perl_sitearch}/auto/Authen/TacacsPlus/TacacsPlus.so
%{_mandir}/man3/*

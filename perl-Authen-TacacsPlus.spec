%include	/usr/lib/rpm/macros.perl
Summary:	Authen-TacacsPlus perl module
Summary(pl):	Modu� perla Authen-TacacsPlus
Name:		perl-Authen-TacacsPlus
Version:	0.16
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen/TacacsPlus-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-TacacsPlus - module for authentication using tacacs+ server.

%description -l pl
Authen-TacacsPlus - modu� do autentykacji przy pomocy serwera tacacs+.

%prep
%setup -q -n TacacsPlus-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

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

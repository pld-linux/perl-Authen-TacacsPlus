%include	/usr/lib/rpm/macros.perl
Summary:	Authen-TacacsPlus perl module
Summary(pl):	Modu³ perla Authen-TacacsPlus
Name:		perl-Authen-TacacsPlus
Version:	0.16
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen/TacacsPlus-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-TacacsPlus - module for authentication using tacacs+ server.

%description -l pl
Authen-TacacsPlus - modu³ do autentykacji przy pomocy serwera tacacs+.

%prep
%setup -q -n TacacsPlus-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded \
	$RPM_BUILD_ROOT/%{perl_sitearch}/auto/Authen/TacacsPlus/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Authen/TacacsPlus
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,readme}.gz

%{perl_sitearch}/Authen/TacacsPlus.pm

%dir %{perl_sitearch}/auto/Authen/TacacsPlus
%{perl_sitearch}/auto/Authen/TacacsPlus/.packlist
%{perl_sitearch}/auto/Authen/TacacsPlus/TacacsPlus.bs
%attr(755,root,root) %{perl_sitearch}/auto/Authen/TacacsPlus/TacacsPlus.so

%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
Summary:	Authen::TacacsPlus perl module
Summary(pl):	Modu³ perla Authen::TacacsPlus
Name:		perl-Authen-TacacsPlus
Version:	0.16
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/TacacsPlus-%{version}.tar.gz
# Source0-md5:	6f5fbe80c677dc75c7f7b71ec05c244b
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::TacacsPlus - module for authentication using tacacs+ server.

%description -l pl
Authen::TacacsPlus - modu³ do autentykacji przy pomocy serwera tacacs+.

%prep
%setup -q -n TacacsPlus-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes readme
%{perl_vendorarch}/Authen/TacacsPlus.pm
%dir %{perl_vendorarch}/auto/Authen/TacacsPlus
%attr(755,root,root) %{perl_vendorarch}/auto/Authen/TacacsPlus/TacacsPlus.so
%{_mandir}/man3/*

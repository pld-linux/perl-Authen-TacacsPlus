#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests hang: require server ?

%define		pdir	Authen
%define		pnam	TacacsPlus
Summary:	Authen::TacacsPlus - Perl extension module for authentication using tacacs+ server
Summary(pl.UTF-8):	Authen::TacacsPlus - moduł Perla do uwierzytelniania przy pomocy serwera tacacs+
Name:		perl-Authen-TacacsPlus
Version:	0.22
Release:	11
License:	custom, distributable
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/Authen-TacacsPlus/Authen-TacacsPlus-%{version}.tar.gz
# Source0-md5:	509f2d176393d80cc2657a9af1424982
URL:		http://search.cpan.org/dist/Authen-TacacsPlus/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::TacacsPlus Perl module allows you to authenticate using
tacacs+ server.

%description -l pl.UTF-8
Moduł Perla Authen::TacacsPlus pozwala na uwierzytelnianie przy pomocy
serwera tacacs+.

%prep
%setup -q -n Authen-TacacsPlus-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Authen/TacacsPlus.pm
%dir %{perl_vendorarch}/auto/Authen/TacacsPlus
%attr(755,root,root) %{perl_vendorarch}/auto/Authen/TacacsPlus/TacacsPlus.so
%{_mandir}/man3/*

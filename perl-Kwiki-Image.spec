%define module	Kwiki-Image
%define name	perl-%{module}
%define version 0.01
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Kwiki Image Plugin
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
License:	GPL
Group:		Development/Perl
BuildRequires:	perl(Kwiki)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin provides more comprehensive support for images in Kwiki.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Kwiki


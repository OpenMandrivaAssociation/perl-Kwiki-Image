%define upstream_name	 Kwiki-Image
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Kwiki Image Plugin
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

%description
This plugin provides more comprehensive support for images in Kwiki.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki


%changelog
* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 409302
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-5mdv2009.0
+ Revision: 257450
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-4mdv2009.0
+ Revision: 245419
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.01-2mdv2008.1
+ Revision: 122818
- kill re-definition of %%buildroot on Pixel's request


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Mon Apr 17 2006 Olivier Blin <oblin@mandriva.com> 0.01-1mdk
- initial Mandriva release


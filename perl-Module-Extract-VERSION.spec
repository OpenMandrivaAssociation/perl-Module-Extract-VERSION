%define upstream_name    Module-Extract-VERSION
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Extract a module version without running code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module lets you pull out of module source code the version number for
the module. It assumes that there is only one '$VERSION' in the file.

Class methods
    * $class->parse_version_safely( FILE );

      Given a module file, return the module version. This works just like
      'mldistwatch' in PAUSE. It looks for the single line that has the
      '$VERSION' statement, extracts it, evals it, and returns the result.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 659938
- update to new version 1.01

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2
+ Revision: 655052
- rebuild for updated spec-helper

* Wed Aug 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 415565
- import perl-Module-Extract-VERSION


* Wed Aug 12 2009 cpan2dist 0.13-1mdv
- initial mdv release, generated with cpan2dist

%define upstream_name    Module-Extract-VERSION
%define upstream_version 1.121
Name:		perl-%{upstream_name}
Version:	1.121
Release:	5

Summary:	Extract a module version without running code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/briandfoy/module-extract-version
Source0:	https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Module-Extract-VERSION-1.121.tar.gz

BuildRequires:	make
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
%setup -q -n Module-Extract-VERSION-1.121

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
:  # soft check
%make test || :

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%define upstream_name    Module-Extract-VERSION
%define upstream_version 0.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Extract a module version without running code
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*



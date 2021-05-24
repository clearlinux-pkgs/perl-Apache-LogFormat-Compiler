#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Apache-LogFormat-Compiler
Version  : 0.36
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Apache-LogFormat-Compiler-0.36.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Apache-LogFormat-Compiler-0.36.tar.gz
Summary  : 'Compile a log format string to perl-code '
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Apache-LogFormat-Compiler-license = %{version}-%{release}
Requires: perl-Apache-LogFormat-Compiler-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
[![Build Status](https://travis-ci.org/kazeburo/Apache-LogFormat-Compiler.svg?branch=master)](https://travis-ci.org/kazeburo/Apache-LogFormat-Compiler)
# NAME

%package dev
Summary: dev components for the perl-Apache-LogFormat-Compiler package.
Group: Development
Provides: perl-Apache-LogFormat-Compiler-devel = %{version}-%{release}
Requires: perl-Apache-LogFormat-Compiler = %{version}-%{release}

%description dev
dev components for the perl-Apache-LogFormat-Compiler package.


%package license
Summary: license components for the perl-Apache-LogFormat-Compiler package.
Group: Default

%description license
license components for the perl-Apache-LogFormat-Compiler package.


%package perl
Summary: perl components for the perl-Apache-LogFormat-Compiler package.
Group: Default
Requires: perl-Apache-LogFormat-Compiler = %{version}-%{release}

%description perl
perl components for the perl-Apache-LogFormat-Compiler package.


%prep
%setup -q -n Apache-LogFormat-Compiler-0.36
cd %{_builddir}/Apache-LogFormat-Compiler-0.36

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Apache-LogFormat-Compiler
cp %{_builddir}/Apache-LogFormat-Compiler-0.36/LICENSE %{buildroot}/usr/share/package-licenses/perl-Apache-LogFormat-Compiler/2c39d05eff7565e4bd58a83e6173e2419ef30aeb
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Apache::LogFormat::Compiler.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Apache-LogFormat-Compiler/2c39d05eff7565e4bd58a83e6173e2419ef30aeb

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Apache/LogFormat/Compiler.pm

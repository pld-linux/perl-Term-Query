#
# Conditional build:
%bcond_with	tests	# perform "make test" (tests are broken)

%define		pdir	Term
%define		pnam	Query
Summary:	Term::Query - table-driven query routine
Summary(pl.UTF-8):	Term::Query - oparta na tablicach funkcja realizująca zapytania
Name:		perl-Term-Query
Version:	2.0
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eba5ba66fdf9e98464472dbc89c49dab
URL:		http://search.cpan.org/dist/Term-Query/
BuildRequires:	perl-Array-PrintCols
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::Query is a Perl 5 module, which performs generalized queries on
various kinds of values. Validation and normalization of input, based
on the type, is automated, as is error reporting and re-solicitation
of input.

%description -l pl.UTF-8
Term::Query to moduł Perla 5 wykonujący uogólnione zapytania dla
różnych rodzajów wartości. Zawiera automatyczną kontrolę poprawności i
normalizację wejścia w zależności od typu, a także zgłaszanie błędów i
ponowne odpytywanie wejścia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Copyright README
%{perl_vendorlib}/Term/Query.pm
%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
%define	pdir	Modem
%define	pnam	Vgetty
Summary:	Modem::Vgetty - interface to vgetty(8)
#Summary(pl):	
Name:		perl-Modem-Vgetty
Version:	0.03
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C<Modem::Vgetty> is an encapsulation object for writing applications for
voice modems using the B<vgetty(8)> or B<vm(8)> package. The answering
machines and sofisticated voice applications can be written using
this module.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*

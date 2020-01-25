%define		pdir	Modem
%define		pnam	Vgetty
Summary:	Modem::Vgetty - interface to vgetty(8)
Summary(pl.UTF-8):	Modem::Vgetty - interfejs do vgetty(8)
Name:		perl-Modem-Vgetty
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	351bb0a027dc6dc9552ead80386e57d3
URL:		http://search.cpan.org/dist/Modem-Vgetty/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modem::Vgetty is an encapsulation object for writing applications for
voice modems using the vgetty(8) or vm(8) package. The answering
machines and sofisticated voice applications can be written using this
module.

%description -l pl.UTF-8
Modem::Vgetty to obiekt hermetyzujący do pisania aplikacji dla modemów
głosowych przy użyciu pakietów vgetty(8) lub vm(8). Można przy użyciu
tego modułu pisać automaty odpowiadające i przemyślne aplikacje
głosowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*

Summary:	microcom-like serial terminal emulator
Summary(pl.UTF-8):   Podobny do microcoma emulator terminala szeregowego
Name:		nanocom
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/%{name}/nanocom.tar.gz
# Source0-md5:	e20c7babfed891b70b669123a30b5ad6
URL:		http://nanocom.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nanocom is a microcom-like serial terminal emulator with scripting
support. The requirement for this program was to be small enough to
fit on a floppy-based Linux distribution - such as the one from Linux
Router Project.

%description -l pl.UTF-8
nanocom jest podobnym do microcoma emulatorem terminala szeregowego z
obsługą skryptów. Program ten ma tak małe wymagania, że nadaje się do
stosowania w dyskietkowych dystrybucjach Linuksa - takich jak
wywodząca się z Linux Router Project.

%prep
%setup -q -c

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*

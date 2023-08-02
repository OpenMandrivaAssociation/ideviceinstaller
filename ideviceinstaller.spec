%define git 20230802

Name:		ideviceinstaller
Version:	1.1.2
Release:	%{?git:0.%{git}.}1
Summary:	Restore firmware files to ios devices
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.libimobiledevice.org/
%if 0%{?git:1}
Source0:	https://github.com/libimobiledevice/ideviceinstaller/archive/refs/heads/master.tar.gz#/%{name}-%{git}.tar.gz
%else
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz
%endif

BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libplist-2.0)
BuildRequires: pkgconfig(libimobiledevice-glue-1.0)
BuildRequires: pkgconfig(libzip) 

%description
A command-line application to restore firmware files to iOS devices

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}

[ -e .tarball-version ] || echo %{version} >.tarball-version

./autogen.sh
%configure

%build
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING README.md
%{_bindir}/ideviceinstaller
%{_mandir}/man1/*

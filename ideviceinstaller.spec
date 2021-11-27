%define git 20211124

Name:		ideviceinstaller
Version:	1.1.2
Release:	1.%{git}.0
Summary:	Restore firmware files to ios devices
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libplist-2.0)
BuildRequires: pkgconfig(libimobiledevice-glue-1.0)
BuildRequires: pkgconfig(libzip) 

%description
A command-line application to restore firmware files to iOS devices

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING README.md
%{_bindir}/ideviceinstaller
%{_mandir}/man1/*

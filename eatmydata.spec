Summary:	A small wrapper to disable fsync and related functions
Name:		eatmydata
Version:	105
Release:	1
Group:		File tools
License:	GPLv3
URL:		https://launchpad.net/libeatmydata
Source0:	https://launchpad.net/libeatmydata/trunk/release-%{version}/+download/libeatmydata-%{version}.tar.gz
Patch0:		fix-it.patch
Provides:	libeatmydata = %{EVRD}

%description
libeatmydata is a small LD_PRELOAD library designed to (transparently) disable
fsync (and friends, like open(O_SYNC)). This has two side-effects: making
software that writes data safely to disk a lot quicker and making this software
no longer crash safe.

DO NOT use libeatmydata on software where you care about what it stores. It's
called libEAT-MY-DATA for a reason.

%prep
%setup -q -n libeatmydata-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_libdir}/*
%{_libexecdir}/eatmydata.sh

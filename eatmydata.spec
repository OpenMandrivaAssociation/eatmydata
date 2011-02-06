Summary:	A small wrapper to disable fsync and related functions
Name:		eatmydata
Version:	26
Release:	%mkrel 1
Group:		File tools
License:	GPLv3
URL:		https://launchpad.net/libeatmydata
Source0:	http://launchpad.net/libeatmydata/trunk/release-26/+download/libeatmydata-26.tar.bz2
Source1:	eatmydata
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	libeatmydata

%description 
LD_PRELOAD library that disables all forms of writing data safely to disk.
fsync() becomes a NO-OP, O_SYNC is removed etc. The idea is to use in
testing to get faster test runs where real durability is not required.

%prep
%setup -q -n libeatmydata-%version

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}/%{_bindir}
install -m 755 %{_sourcedir}/%{name} %{buildroot}/%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/%{name}
%{_libdir}/*

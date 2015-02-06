Summary:	A small wrapper to disable fsync and related functions
Name:		eatmydata
Version:	65
Release:	2
Group:		File tools
License:	GPLv3
URL:		https://launchpad.net/libeatmydata
Source0:	https://launchpad.net/libeatmydata/trunk/release-%{version}/+download/libeatmydata-%{version}.tar.gz
Source1:	eatmydata
Patch0:		libeatmydata-26-use-correct-libdir.patch
Provides:	libeatmydata

%description 
LD_PRELOAD library that disables all forms of writing data safely to disk.
fsync() becomes a NO-OP, O_SYNC is removed etc. The idea is to use in
testing to get faster test runs where real durability is not required.

%prep
%setup -q -n libeatmydata-%{version}
#patch0 -p1

%build
#./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
 # LIBDIR=%{_libdir} DESTDIR=%{buildroot}

install -d %{buildroot}/%{_bindir}
install -m 755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}
sed -i 's,__LIBDIR__,%{_libdir},g' %{buildroot}/%{_bindir}/%{name}

%files
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_libdir}/libeatmydata.so*
%{_libexecdir}/eatmydata.sh


%changelog
* Sun Feb 06 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 26-1mdv2011.0
+ Revision: 636355
- added patch to use correct libdir
- imported package eatmydata


%define _default_patch_fuzz 2

Summary: Create identical zip files over multiple systems
Name: torrentzip
Version: 0.2
Release: 3%{?dist}
License: GPL
Group: Applications/File
URL: http://sourceforge.net/projects/trrntzip
Source: http://dl.sf.net/trrntzip/trrntzip_v02_src.tar.gz
Patch0: patch-src-trrntzip.c
Patch1: trrntzip-0.2-warningfixes.patch
Patch2: trrntzip-0.2-help.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel
BuildRequires: autoconf, automake, libtool

%description
TorrentZip is a replacement for MameZip. The goal of the program is to use
standard values when creating zips to create identical files over multiple
systems.


%prep
%setup -n trrntzip
%patch0 -p0 -b .chmod
%patch1 -p1 -b .warningfixes
%patch2 -p1 -b .help


%build
# No configure, we need to generate it from configure.in
./autogen.sh
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_bindir}/trrntzip


%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.2-3
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.2-2
- rebuild for RPM Fusion
- define _default_patch_fuzz 2

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 0.2-1
- Initial RPM release.


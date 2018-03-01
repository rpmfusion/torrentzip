# We patch the same files multiple times, so we have slight differences
%define _default_patch_fuzz 2

Summary: Create identical zip files over multiple systems
Name: torrentzip
Version: 0.2
Release: 11%{?dist}
License: GPLv2+
Group: Applications/File
URL: http://sourceforge.net/projects/trrntzip
Source: http://dl.sf.net/trrntzip/trrntzip_v02_src.tar.gz
Patch0: trrntzip-0.2-chmod.patch
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
%setup -q -n trrntzip
%patch0 -p0 -b .chmod
%patch1 -p1 -b .warningfixes
%patch2 -p1 -b .help


%build
# No configure, we need to generate it from configure.in
./autogen.sh
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING README
%{_bindir}/trrntzip


%changelog
* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.2-7
- Mass rebuilt for Fedora 19 Features

* Wed Apr  4 2012 Matthias Saou <matthias@saou.eu> 0.2-6
- Minor spec file cleanups.
- Update license field.
- Rename patch0 to be more explicit.

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.2-3
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.2-2
- rebuild for RPM Fusion
- define _default_patch_fuzz 2

* Tue Jan  9 2007 Matthias Saou <matthias@saou.eu> 0.2-1
- Initial RPM release.


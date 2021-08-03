# We patch the same files multiple times, so we have slight differences
%define _default_patch_fuzz 2

Summary: Create identical zip files over multiple systems
Name: torrentzip
Version: 0.9
Release: 6%{?dist}
License: GPLv2+
Group: Applications/File
URL: http://sourceforge.net/projects/trrntzip
Source: https://sourceforge.net/code-snapshots/svn/t/tr/trrntzip/code/trrntzip-code-r9.zip
Patch0: torrentzip-0.9-format-secure.patch
Patch1: trrntzip-0.2-warningfixes.patch
Patch2: trrntzip-0.2-help.patch
BuildRequires: zlib-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
TorrentZip is a replacement for MameZip. The goal of the program is to use
standard values when creating zips to create identical files over multiple
systems.


%prep
%setup -q -n trrntzip-code-r9
%patch0 -p1 -b .format_secure
#patch1 -p1 -b .warningfixes
#patch2 -p1 -b .help


%build
# No configure, we need to generate it from configure.in
sh ./autogen.sh
%configure
%make_build


%install
%make_install


%files
%doc AUTHORS COPYING README
%{_bindir}/trrntzip


%changelog
* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Sérgio Basto <sergio@serjux.com> - 0.9-1
- Torrentzip 0.9 from git source

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.2-13
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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


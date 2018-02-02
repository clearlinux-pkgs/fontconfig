#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fontconfig
Version  : 2.12.6
Release  : 30
URL      : https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.12.6.tar.gz
Source0  : https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.12.6.tar.gz
Source1  : fontconfig-trigger.service
Summary  : Font configuration and customization library
Group    : Development/Tools
License  : HPND MIT
Requires: fontconfig-bin
Requires: fontconfig-config
Requires: fontconfig-lib
Requires: fontconfig-data
Requires: fontconfig-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : fontconfig-data
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gperf
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32expat)
BuildRequires : pkgconfig(32freetype2)
BuildRequires : pkgconfig(32libxml-2.0)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : python-dev
Patch1: 0001-Include-stateless-configuration.patch
Patch2: 0002-Use-sane-defaults-throughout-the-system.patch
Patch3: 0003-Enforce-antialiasing-by-default.patch

%description
Fontconfig is designed to locate fonts within the
system and select them according to requirements specified by 
applications.

%package bin
Summary: bin components for the fontconfig package.
Group: Binaries
Requires: fontconfig-data
Requires: fontconfig-config

%description bin
bin components for the fontconfig package.


%package config
Summary: config components for the fontconfig package.
Group: Default

%description config
config components for the fontconfig package.


%package data
Summary: data components for the fontconfig package.
Group: Data

%description data
data components for the fontconfig package.


%package dev
Summary: dev components for the fontconfig package.
Group: Development
Requires: fontconfig-lib
Requires: fontconfig-bin
Requires: fontconfig-data
Provides: fontconfig-devel

%description dev
dev components for the fontconfig package.


%package dev32
Summary: dev32 components for the fontconfig package.
Group: Default
Requires: fontconfig-lib32
Requires: fontconfig-bin
Requires: fontconfig-data
Requires: fontconfig-dev

%description dev32
dev32 components for the fontconfig package.


%package doc
Summary: doc components for the fontconfig package.
Group: Documentation

%description doc
doc components for the fontconfig package.


%package lib
Summary: lib components for the fontconfig package.
Group: Libraries
Requires: fontconfig-data

%description lib
lib components for the fontconfig package.


%package lib32
Summary: lib32 components for the fontconfig package.
Group: Default
Requires: fontconfig-data

%description lib32
lib32 components for the fontconfig package.


%prep
%setup -q -n fontconfig-2.12.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a fontconfig-2.12.6 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511462433
%reconfigure --disable-static --sysconfdir=/usr/share/defaults
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static --sysconfdir=/usr/share/defaults  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1511462433
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/fontconfig-trigger.service
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/
ln -s ../fontconfig-trigger.service  %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/fontconfig-trigger.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fc-cache
/usr/bin/fc-cat
/usr/bin/fc-list
/usr/bin/fc-match
/usr/bin/fc-pattern
/usr/bin/fc-query
/usr/bin/fc-scan
/usr/bin/fc-validate

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/fontconfig-trigger.service
/usr/lib/systemd/system/update-triggers.target.wants/fontconfig-trigger.service

%files data
%defattr(-,root,root,-)
/usr/share/defaults/fonts/conf.d/10-hinting-slight.conf
/usr/share/defaults/fonts/conf.d/10-scale-bitmap-fonts.conf
/usr/share/defaults/fonts/conf.d/20-unhint-small-vera.conf
/usr/share/defaults/fonts/conf.d/30-metric-aliases.conf
/usr/share/defaults/fonts/conf.d/40-nonlatin.conf
/usr/share/defaults/fonts/conf.d/45-generic.conf
/usr/share/defaults/fonts/conf.d/45-latin.conf
/usr/share/defaults/fonts/conf.d/49-sansserif.conf
/usr/share/defaults/fonts/conf.d/50-user.conf
/usr/share/defaults/fonts/conf.d/51-local.conf
/usr/share/defaults/fonts/conf.d/60-generic.conf
/usr/share/defaults/fonts/conf.d/60-latin.conf
/usr/share/defaults/fonts/conf.d/65-fonts-persian.conf
/usr/share/defaults/fonts/conf.d/65-nonlatin.conf
/usr/share/defaults/fonts/conf.d/69-unifont.conf
/usr/share/defaults/fonts/conf.d/80-delicious.conf
/usr/share/defaults/fonts/conf.d/90-synthetic.conf
/usr/share/defaults/fonts/conf.d/README
/usr/share/defaults/fonts/fonts.conf
/usr/share/defaults/fonts/fonts.conf.bak
/usr/share/fontconfig/conf.avail/10-antialiasing.conf
/usr/share/fontconfig/conf.avail/10-autohint.conf
/usr/share/fontconfig/conf.avail/10-hinting-full.conf
/usr/share/fontconfig/conf.avail/10-hinting-medium.conf
/usr/share/fontconfig/conf.avail/10-hinting-none.conf
/usr/share/fontconfig/conf.avail/10-hinting-slight.conf
/usr/share/fontconfig/conf.avail/10-no-sub-pixel.conf
/usr/share/fontconfig/conf.avail/10-scale-bitmap-fonts.conf
/usr/share/fontconfig/conf.avail/10-sub-pixel-bgr.conf
/usr/share/fontconfig/conf.avail/10-sub-pixel-rgb.conf
/usr/share/fontconfig/conf.avail/10-sub-pixel-vbgr.conf
/usr/share/fontconfig/conf.avail/10-sub-pixel-vrgb.conf
/usr/share/fontconfig/conf.avail/10-unhinted.conf
/usr/share/fontconfig/conf.avail/11-lcdfilter-default.conf
/usr/share/fontconfig/conf.avail/11-lcdfilter-legacy.conf
/usr/share/fontconfig/conf.avail/11-lcdfilter-light.conf
/usr/share/fontconfig/conf.avail/20-unhint-small-vera.conf
/usr/share/fontconfig/conf.avail/25-unhint-nonlatin.conf
/usr/share/fontconfig/conf.avail/30-metric-aliases.conf
/usr/share/fontconfig/conf.avail/40-nonlatin.conf
/usr/share/fontconfig/conf.avail/45-generic.conf
/usr/share/fontconfig/conf.avail/45-latin.conf
/usr/share/fontconfig/conf.avail/49-sansserif.conf
/usr/share/fontconfig/conf.avail/50-user.conf
/usr/share/fontconfig/conf.avail/51-local.conf
/usr/share/fontconfig/conf.avail/60-generic.conf
/usr/share/fontconfig/conf.avail/60-latin.conf
/usr/share/fontconfig/conf.avail/65-fonts-persian.conf
/usr/share/fontconfig/conf.avail/65-khmer.conf
/usr/share/fontconfig/conf.avail/65-nonlatin.conf
/usr/share/fontconfig/conf.avail/69-unifont.conf
/usr/share/fontconfig/conf.avail/70-no-bitmaps.conf
/usr/share/fontconfig/conf.avail/70-yes-bitmaps.conf
/usr/share/fontconfig/conf.avail/80-delicious.conf
/usr/share/fontconfig/conf.avail/90-synthetic.conf
/usr/share/xml/fontconfig/fonts.dtd

%files dev
%defattr(-,root,root,-)
/usr/include/fontconfig/fcfreetype.h
/usr/include/fontconfig/fcprivate.h
/usr/include/fontconfig/fontconfig.h
/usr/lib64/libfontconfig.so
/usr/lib64/pkgconfig/fontconfig.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfontconfig.so
/usr/lib32/pkgconfig/32fontconfig.pc
/usr/lib32/pkgconfig/fontconfig.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/fontconfig/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfontconfig.so.1
/usr/lib64/libfontconfig.so.1.10.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfontconfig.so.1
/usr/lib32/libfontconfig.so.1.10.1

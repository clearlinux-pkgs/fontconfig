#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fontconfig
Version  : 2.13.1
Release  : 45
URL      : https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.13.1.tar.gz
Source0  : https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.13.1.tar.gz
Source1  : fontconfig-trigger.service
Summary  : Font configuration and customization library
Group    : Development/Tools
License  : HPND MIT
Requires: fontconfig-bin = %{version}-%{release}
Requires: fontconfig-data = %{version}-%{release}
Requires: fontconfig-filemap = %{version}-%{release}
Requires: fontconfig-lib = %{version}-%{release}
Requires: fontconfig-license = %{version}-%{release}
Requires: fontconfig-locales = %{version}-%{release}
Requires: fontconfig-man = %{version}-%{release}
Requires: fontconfig-services = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : fontconfig-data
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gperf
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32expat)
BuildRequires : pkgconfig(32freetype2)
BuildRequires : pkgconfig(32json-c)
BuildRequires : pkgconfig(32libxml-2.0)
BuildRequires : pkgconfig(32uuid)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(uuid)
Patch1: 0001-Include-stateless-configuration.patch
Patch2: 0002-Add-spacing-config-for-Clear-Sans.patch
Patch3: 0003-Use-sane-defaults-throughout-the-system.patch
Patch4: 0004-Enforce-antialiasing-by-default.patch

%description
Fontconfig is designed to locate fonts within the
system and select them according to requirements specified by 
applications.

%package bin
Summary: bin components for the fontconfig package.
Group: Binaries
Requires: fontconfig-data = %{version}-%{release}
Requires: fontconfig-license = %{version}-%{release}
Requires: fontconfig-services = %{version}-%{release}
Requires: fontconfig-filemap = %{version}-%{release}

%description bin
bin components for the fontconfig package.


%package data
Summary: data components for the fontconfig package.
Group: Data

%description data
data components for the fontconfig package.


%package dev
Summary: dev components for the fontconfig package.
Group: Development
Requires: fontconfig-lib = %{version}-%{release}
Requires: fontconfig-bin = %{version}-%{release}
Requires: fontconfig-data = %{version}-%{release}
Provides: fontconfig-devel = %{version}-%{release}
Requires: fontconfig = %{version}-%{release}

%description dev
dev components for the fontconfig package.


%package dev32
Summary: dev32 components for the fontconfig package.
Group: Default
Requires: fontconfig-lib32 = %{version}-%{release}
Requires: fontconfig-bin = %{version}-%{release}
Requires: fontconfig-data = %{version}-%{release}
Requires: fontconfig-dev = %{version}-%{release}

%description dev32
dev32 components for the fontconfig package.


%package doc
Summary: doc components for the fontconfig package.
Group: Documentation
Requires: fontconfig-man = %{version}-%{release}

%description doc
doc components for the fontconfig package.


%package filemap
Summary: filemap components for the fontconfig package.
Group: Default

%description filemap
filemap components for the fontconfig package.


%package lib
Summary: lib components for the fontconfig package.
Group: Libraries
Requires: fontconfig-data = %{version}-%{release}
Requires: fontconfig-license = %{version}-%{release}
Requires: fontconfig-filemap = %{version}-%{release}

%description lib
lib components for the fontconfig package.


%package lib32
Summary: lib32 components for the fontconfig package.
Group: Default
Requires: fontconfig-data = %{version}-%{release}
Requires: fontconfig-license = %{version}-%{release}

%description lib32
lib32 components for the fontconfig package.


%package license
Summary: license components for the fontconfig package.
Group: Default

%description license
license components for the fontconfig package.


%package locales
Summary: locales components for the fontconfig package.
Group: Default

%description locales
locales components for the fontconfig package.


%package man
Summary: man components for the fontconfig package.
Group: Default

%description man
man components for the fontconfig package.


%package services
Summary: services components for the fontconfig package.
Group: Systemd services

%description services
services components for the fontconfig package.


%prep
%setup -q -n fontconfig-2.13.1
cd %{_builddir}/fontconfig-2.13.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
pushd ..
cp -a fontconfig-2.13.1 build32
popd
pushd ..
cp -a fontconfig-2.13.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634687283
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%reconfigure --disable-static --sysconfdir=/usr/share/defaults
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static --sysconfdir=/usr/share/defaults  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static --sysconfdir=/usr/share/defaults
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1634687283
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fontconfig
cp %{_builddir}/fontconfig-2.13.1/COPYING %{buildroot}/usr/share/package-licenses/fontconfig/ae92a5e66650b2e46038f56b0159851840513476
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang fontconfig-conf
%find_lang fontconfig
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/fontconfig-trigger.service
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/
ln -s ../fontconfig-trigger.service  %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/fontconfig-trigger.service
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fc-cache
/usr/bin/fc-cat
/usr/bin/fc-conflist
/usr/bin/fc-list
/usr/bin/fc-match
/usr/bin/fc-pattern
/usr/bin/fc-query
/usr/bin/fc-scan
/usr/bin/fc-validate
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/defaults/fonts/conf.d/10-hinting-slight.conf
/usr/share/defaults/fonts/conf.d/10-scale-bitmap-fonts.conf
/usr/share/defaults/fonts/conf.d/20-unhint-clear-sans.conf
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
/usr/share/fontconfig/conf.avail/20-unhint-clear-sans.conf
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
/usr/share/gettext/its/fontconfig.its
/usr/share/gettext/its/fontconfig.loc
/usr/share/xml/fontconfig/fonts.dtd

%files dev
%defattr(-,root,root,-)
/usr/include/fontconfig/fcfreetype.h
/usr/include/fontconfig/fcprivate.h
/usr/include/fontconfig/fontconfig.h
/usr/lib64/libfontconfig.so
/usr/lib64/pkgconfig/fontconfig.pc
/usr/share/man/man3/FcAtomicCreate.3
/usr/share/man/man3/FcAtomicDeleteNew.3
/usr/share/man/man3/FcAtomicDestroy.3
/usr/share/man/man3/FcAtomicLock.3
/usr/share/man/man3/FcAtomicNewFile.3
/usr/share/man/man3/FcAtomicOrigFile.3
/usr/share/man/man3/FcAtomicReplaceOrig.3
/usr/share/man/man3/FcAtomicUnlock.3
/usr/share/man/man3/FcBlanksAdd.3
/usr/share/man/man3/FcBlanksCreate.3
/usr/share/man/man3/FcBlanksDestroy.3
/usr/share/man/man3/FcBlanksIsMember.3
/usr/share/man/man3/FcCacheCopySet.3
/usr/share/man/man3/FcCacheCreateTagFile.3
/usr/share/man/man3/FcCacheDir.3
/usr/share/man/man3/FcCacheNumFont.3
/usr/share/man/man3/FcCacheNumSubdir.3
/usr/share/man/man3/FcCacheSubdir.3
/usr/share/man/man3/FcCharSetAddChar.3
/usr/share/man/man3/FcCharSetCopy.3
/usr/share/man/man3/FcCharSetCount.3
/usr/share/man/man3/FcCharSetCoverage.3
/usr/share/man/man3/FcCharSetCreate.3
/usr/share/man/man3/FcCharSetDelChar.3
/usr/share/man/man3/FcCharSetDestroy.3
/usr/share/man/man3/FcCharSetEqual.3
/usr/share/man/man3/FcCharSetFirstPage.3
/usr/share/man/man3/FcCharSetHasChar.3
/usr/share/man/man3/FcCharSetIntersect.3
/usr/share/man/man3/FcCharSetIntersectCount.3
/usr/share/man/man3/FcCharSetIsSubset.3
/usr/share/man/man3/FcCharSetMerge.3
/usr/share/man/man3/FcCharSetNew.3
/usr/share/man/man3/FcCharSetNextPage.3
/usr/share/man/man3/FcCharSetSubtract.3
/usr/share/man/man3/FcCharSetSubtractCount.3
/usr/share/man/man3/FcCharSetUnion.3
/usr/share/man/man3/FcConfigAppFontAddDir.3
/usr/share/man/man3/FcConfigAppFontAddFile.3
/usr/share/man/man3/FcConfigAppFontClear.3
/usr/share/man/man3/FcConfigBuildFonts.3
/usr/share/man/man3/FcConfigCreate.3
/usr/share/man/man3/FcConfigDestroy.3
/usr/share/man/man3/FcConfigEnableHome.3
/usr/share/man/man3/FcConfigFileInfoIterGet.3
/usr/share/man/man3/FcConfigFileInfoIterInit.3
/usr/share/man/man3/FcConfigFileInfoIterNext.3
/usr/share/man/man3/FcConfigFilename.3
/usr/share/man/man3/FcConfigGetBlanks.3
/usr/share/man/man3/FcConfigGetCache.3
/usr/share/man/man3/FcConfigGetCacheDirs.3
/usr/share/man/man3/FcConfigGetConfigDirs.3
/usr/share/man/man3/FcConfigGetConfigFiles.3
/usr/share/man/man3/FcConfigGetCurrent.3
/usr/share/man/man3/FcConfigGetFontDirs.3
/usr/share/man/man3/FcConfigGetFonts.3
/usr/share/man/man3/FcConfigGetRescanInterval.3
/usr/share/man/man3/FcConfigGetSysRoot.3
/usr/share/man/man3/FcConfigHome.3
/usr/share/man/man3/FcConfigParseAndLoad.3
/usr/share/man/man3/FcConfigParseAndLoadFromMemory.3
/usr/share/man/man3/FcConfigReference.3
/usr/share/man/man3/FcConfigSetCurrent.3
/usr/share/man/man3/FcConfigSetRescanInterval.3
/usr/share/man/man3/FcConfigSetSysRoot.3
/usr/share/man/man3/FcConfigSubstitute.3
/usr/share/man/man3/FcConfigSubstituteWithPat.3
/usr/share/man/man3/FcConfigUptoDate.3
/usr/share/man/man3/FcDefaultSubstitute.3
/usr/share/man/man3/FcDirCacheClean.3
/usr/share/man/man3/FcDirCacheCreateUUID.3
/usr/share/man/man3/FcDirCacheDeleteUUID.3
/usr/share/man/man3/FcDirCacheLoad.3
/usr/share/man/man3/FcDirCacheLoadFile.3
/usr/share/man/man3/FcDirCacheRead.3
/usr/share/man/man3/FcDirCacheRescan.3
/usr/share/man/man3/FcDirCacheUnlink.3
/usr/share/man/man3/FcDirCacheUnload.3
/usr/share/man/man3/FcDirCacheValid.3
/usr/share/man/man3/FcDirSave.3
/usr/share/man/man3/FcDirScan.3
/usr/share/man/man3/FcFileIsDir.3
/usr/share/man/man3/FcFileScan.3
/usr/share/man/man3/FcFini.3
/usr/share/man/man3/FcFontList.3
/usr/share/man/man3/FcFontMatch.3
/usr/share/man/man3/FcFontRenderPrepare.3
/usr/share/man/man3/FcFontSetAdd.3
/usr/share/man/man3/FcFontSetCreate.3
/usr/share/man/man3/FcFontSetDestroy.3
/usr/share/man/man3/FcFontSetList.3
/usr/share/man/man3/FcFontSetMatch.3
/usr/share/man/man3/FcFontSetPrint.3
/usr/share/man/man3/FcFontSetSort.3
/usr/share/man/man3/FcFontSetSortDestroy.3
/usr/share/man/man3/FcFontSort.3
/usr/share/man/man3/FcFreeTypeCharIndex.3
/usr/share/man/man3/FcFreeTypeCharSet.3
/usr/share/man/man3/FcFreeTypeCharSetAndSpacing.3
/usr/share/man/man3/FcFreeTypeQuery.3
/usr/share/man/man3/FcFreeTypeQueryAll.3
/usr/share/man/man3/FcFreeTypeQueryFace.3
/usr/share/man/man3/FcGetDefaultLangs.3
/usr/share/man/man3/FcGetLangs.3
/usr/share/man/man3/FcGetVersion.3
/usr/share/man/man3/FcInit.3
/usr/share/man/man3/FcInitBringUptoDate.3
/usr/share/man/man3/FcInitLoadConfig.3
/usr/share/man/man3/FcInitLoadConfigAndFonts.3
/usr/share/man/man3/FcInitReinitialize.3
/usr/share/man/man3/FcIsLower.3
/usr/share/man/man3/FcIsUpper.3
/usr/share/man/man3/FcLangGetCharSet.3
/usr/share/man/man3/FcLangNormalize.3
/usr/share/man/man3/FcLangSetAdd.3
/usr/share/man/man3/FcLangSetCompare.3
/usr/share/man/man3/FcLangSetContains.3
/usr/share/man/man3/FcLangSetCopy.3
/usr/share/man/man3/FcLangSetCreate.3
/usr/share/man/man3/FcLangSetDel.3
/usr/share/man/man3/FcLangSetDestroy.3
/usr/share/man/man3/FcLangSetEqual.3
/usr/share/man/man3/FcLangSetGetLangs.3
/usr/share/man/man3/FcLangSetHasLang.3
/usr/share/man/man3/FcLangSetHash.3
/usr/share/man/man3/FcLangSetSubtract.3
/usr/share/man/man3/FcLangSetUnion.3
/usr/share/man/man3/FcMatrixCopy.3
/usr/share/man/man3/FcMatrixEqual.3
/usr/share/man/man3/FcMatrixInit.3
/usr/share/man/man3/FcMatrixMultiply.3
/usr/share/man/man3/FcMatrixRotate.3
/usr/share/man/man3/FcMatrixScale.3
/usr/share/man/man3/FcMatrixShear.3
/usr/share/man/man3/FcNameConstant.3
/usr/share/man/man3/FcNameGetConstant.3
/usr/share/man/man3/FcNameGetObjectType.3
/usr/share/man/man3/FcNameParse.3
/usr/share/man/man3/FcNameRegisterConstants.3
/usr/share/man/man3/FcNameRegisterObjectTypes.3
/usr/share/man/man3/FcNameUnparse.3
/usr/share/man/man3/FcNameUnregisterConstants.3
/usr/share/man/man3/FcNameUnregisterObjectTypes.3
/usr/share/man/man3/FcObjectSetAdd.3
/usr/share/man/man3/FcObjectSetBuild.3
/usr/share/man/man3/FcObjectSetCreate.3
/usr/share/man/man3/FcObjectSetDestroy.3
/usr/share/man/man3/FcPatternAdd-Type.3
/usr/share/man/man3/FcPatternAdd.3
/usr/share/man/man3/FcPatternAddWeak.3
/usr/share/man/man3/FcPatternBuild.3
/usr/share/man/man3/FcPatternCreate.3
/usr/share/man/man3/FcPatternDel.3
/usr/share/man/man3/FcPatternDestroy.3
/usr/share/man/man3/FcPatternDuplicate.3
/usr/share/man/man3/FcPatternEqual.3
/usr/share/man/man3/FcPatternEqualSubset.3
/usr/share/man/man3/FcPatternFilter.3
/usr/share/man/man3/FcPatternFindIter.3
/usr/share/man/man3/FcPatternFormat.3
/usr/share/man/man3/FcPatternGet-Type.3
/usr/share/man/man3/FcPatternGet.3
/usr/share/man/man3/FcPatternGetWithBinding.3
/usr/share/man/man3/FcPatternHash.3
/usr/share/man/man3/FcPatternIterEqual.3
/usr/share/man/man3/FcPatternIterGetObject.3
/usr/share/man/man3/FcPatternIterGetValue.3
/usr/share/man/man3/FcPatternIterIsValid.3
/usr/share/man/man3/FcPatternIterNext.3
/usr/share/man/man3/FcPatternIterStart.3
/usr/share/man/man3/FcPatternIterValueCount.3
/usr/share/man/man3/FcPatternObjectCount.3
/usr/share/man/man3/FcPatternPrint.3
/usr/share/man/man3/FcPatternReference.3
/usr/share/man/man3/FcPatternRemove.3
/usr/share/man/man3/FcRangeCopy.3
/usr/share/man/man3/FcRangeCreateDouble.3
/usr/share/man/man3/FcRangeCreateInteger.3
/usr/share/man/man3/FcRangeDestroy.3
/usr/share/man/man3/FcRangeGetDouble.3
/usr/share/man/man3/FcStrBasename.3
/usr/share/man/man3/FcStrCmp.3
/usr/share/man/man3/FcStrCmpIgnoreCase.3
/usr/share/man/man3/FcStrCopy.3
/usr/share/man/man3/FcStrCopyFilename.3
/usr/share/man/man3/FcStrDirname.3
/usr/share/man/man3/FcStrDowncase.3
/usr/share/man/man3/FcStrFree.3
/usr/share/man/man3/FcStrListCreate.3
/usr/share/man/man3/FcStrListDone.3
/usr/share/man/man3/FcStrListFirst.3
/usr/share/man/man3/FcStrListNext.3
/usr/share/man/man3/FcStrPlus.3
/usr/share/man/man3/FcStrSetAdd.3
/usr/share/man/man3/FcStrSetAddFilename.3
/usr/share/man/man3/FcStrSetCreate.3
/usr/share/man/man3/FcStrSetDel.3
/usr/share/man/man3/FcStrSetDestroy.3
/usr/share/man/man3/FcStrSetEqual.3
/usr/share/man/man3/FcStrSetMember.3
/usr/share/man/man3/FcStrStr.3
/usr/share/man/man3/FcStrStrIgnoreCase.3
/usr/share/man/man3/FcToLower.3
/usr/share/man/man3/FcUcs4ToUtf8.3
/usr/share/man/man3/FcUtf16Len.3
/usr/share/man/man3/FcUtf16ToUcs4.3
/usr/share/man/man3/FcUtf8Len.3
/usr/share/man/man3/FcUtf8ToUcs4.3
/usr/share/man/man3/FcValueDestroy.3
/usr/share/man/man3/FcValueEqual.3
/usr/share/man/man3/FcValuePrint.3
/usr/share/man/man3/FcValueSave.3
/usr/share/man/man3/FcWeightFromOpenType.3
/usr/share/man/man3/FcWeightFromOpenTypeDouble.3
/usr/share/man/man3/FcWeightToOpenType.3
/usr/share/man/man3/FcWeightToOpenTypeDouble.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfontconfig.so
/usr/lib32/pkgconfig/32fontconfig.pc
/usr/lib32/pkgconfig/fontconfig.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/fontconfig/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-fontconfig

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfontconfig.so.1
/usr/lib64/libfontconfig.so.1.12.0
/usr/share/clear/optimized-elf/lib*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfontconfig.so.1
/usr/lib32/libfontconfig.so.1.12.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fontconfig/ae92a5e66650b2e46038f56b0159851840513476

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fc-cache.1
/usr/share/man/man1/fc-cat.1
/usr/share/man/man1/fc-conflist.1
/usr/share/man/man1/fc-list.1
/usr/share/man/man1/fc-match.1
/usr/share/man/man1/fc-pattern.1
/usr/share/man/man1/fc-query.1
/usr/share/man/man1/fc-scan.1
/usr/share/man/man1/fc-validate.1
/usr/share/man/man5/fonts-conf.5

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fontconfig-trigger.service
/usr/lib/systemd/system/update-triggers.target.wants/fontconfig-trigger.service

%files locales -f fontconfig-conf.lang -f fontconfig.lang
%defattr(-,root,root,-)


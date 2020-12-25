%undefine __cmake_in_source_build

%global appname Quotient
%global libname lib%{appname}

Name: libquotient
Version: 0.6.3
Release: 1%{?dist}

License: LGPLv2+
URL: https://github.com/quotient-im/%{libname}
Summary: Qt5 library to write cross-platform clients for Matrix
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%if 0%{?fedora} && 0%{?fedora} >= 34
Provides: libqmatrixclient = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: libqmatrixclient < %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description
The Quotient project aims to produce a Qt5-based SDK to develop applications
for Matrix. libQuotient is a library that enables client applications. It is
the backbone of Quaternion, Spectral and other projects. Versions 0.5.x and
older use the previous name - libQMatrixClient.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?fedora} && 0%{?fedora} >= 34
Provides: libqmatrixclient-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: libqmatrixclient-devel < %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description devel
%{summary}.

%prep
%autosetup -n %{libname}-%{version}
rm -rf 3rdparty

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DQuotient_INSTALL_TESTS:BOOL=OFF \
    -DQuotient_INSTALL_EXAMPLE:BOOL=OFF \
    -DQuotient_ENABLE_E2EE:BOOL=ON \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH="include/%{appname}"
%cmake_build

%check
%ctest

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/ndk-modules

%files
%license COPYING
%doc README.md CONTRIBUTING.md SECURITY.md
%{_libdir}/%{libname}.so.0*

%files devel
%{_includedir}/%{appname}/
%{_libdir}/cmake/%{appname}/
%{_libdir}/pkgconfig/%{appname}.pc
%{_libdir}/%{libname}.so

%changelog
* Fri Dec 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.3-1
- Updated to version 0.6.3.

* Sat Oct 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.2-1
- Updated to version 0.6.2.

* Sat Sep 05 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.1-1
- Updated to version 0.6.1.

* Wed Jul 29 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Sat Mar 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.4.20200207git9bcf0cb
- Updated to latest Git snapshot.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.3.20200121gite3a5b3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.2.20200121gite3a5b3a
- Updated to version 0.6.0-git.

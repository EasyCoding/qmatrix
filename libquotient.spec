%global appname Quotient
%global libname lib%{appname}

%global commit0 88d69a360090f8c027746358c6625224673113bf
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20191013

Name: libquotient
Summary: A Qt5 library to write cross-platform clients for Matrix
Version: 0.5.2
Release: 0.3.%{date}git%{shortcommit0}%{?dist}

License: LGPLv2.1
URL: https://github.com/quotient-im/%{libname}

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

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

%description
The Quotient project aims to produce a Qt5-based SDK to develop
applications for Matrix. libQuotient is a library that enables
client applications. It is the backbone of Quaternion, Spectral
and other projects. Versions 0.5.x and older use the previous
name - libQMatrixClient.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{libname}-%{commit0}
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DQUOTIENT_INSTALL_EXAMPLE=OFF \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
%ninja_install -C %{_target_platform}
rm -rf %{buildroot}%{_datadir}/ndk-modules

%files
%license COPYING
%doc README.md CONTRIBUTING.md SECURITY.md
%{_libdir}/%{libname}.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/%{appname}.pc
%{_libdir}/cmake/%{appname}
%{_libdir}/%{libname}.so

%changelog
* Wed Oct 16 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.2-0.3.20191013git88d69a3
- Updated to latest Git snapshot.

* Tue Oct 01 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.2-0.2.20191001gitf240074
- Updated to latest Git snapshot.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.2-0.1.20190816git8663c2e
- Initial SPEC release.

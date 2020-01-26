%global appname Quotient
%global libname lib%{appname}

%global commit0 e3a5b3a5e5253fc5ce67574b01e8d25ec14e4d25
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20200121

Name: libquotient
Version: 0.6.0
Release: 0.2.%{date}git%{shortcommit0}%{?dist}

License: LGPLv2+
URL: https://github.com/quotient-im/%{libname}
Summary: Qt5 library to write cross-platform clients for Matrix
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

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
The Quotient project aims to produce a Qt5-based SDK to develop applications
for Matrix. libQuotient is a library that enables client applications. It is
the backbone of Quaternion, Spectral and other projects. Versions 0.5.x and
older use the previous name - libQMatrixClient.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{libname}-%{commit0}
mkdir -p %{_target_platform}
rm -rf 3rdparty

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DQUOTIENT_INSTALL_EXAMPLE=OFF \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH="include/%{appname}" \
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
%{_libdir}/%{libname}.so.0*

%files devel
%{_includedir}/%{appname}/
%{_libdir}/cmake/%{appname}/
%{_libdir}/pkgconfig/%{appname}.pc
%{_libdir}/%{libname}.so

%changelog
* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.2.20200121gite3a5b3a
- Updated to version 0.6.0-git.

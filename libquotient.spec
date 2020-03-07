%global appname Quotient
%global libname lib%{appname}

%global commit0 9bcf0cbc3d690663d37d1737173ab5088fed152f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20200207

Name: libquotient
Version: 0.6.0
Release: 0.4.%{date}git%{shortcommit0}%{?dist}

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

# It looks like Qt is broken on s390x. Linkage failure with QByteArray.
ExcludeArch: s390x

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
* Sat Mar 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.4.20200207git9bcf0cb
- Updated to latest Git snapshot.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.3.20200121gite3a5b3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.2.20200121gite3a5b3a
- Updated to version 0.6.0-git.

%global appname Quotient
%global libname lib%{appname}

%global commit0 8663c2e78407a0c0df872eaf9bb6b41de2fbdc9e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20190816

Name: libquotient
Summary: A Qt5 library to write cross-platform clients for Matrix
Version: 0.5.2
Release: 0.1.%{date}git%{shortcommit0}%{?dist}

License: LGPLv2.1
URL: https://github.com/quotient-im/%{libname}

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: libolm-devel
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
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
%ninja_install -C %{_target_platform}

%files
%license COPYING
%doc README.md CONTRIBUTING.md SECURITY.md
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{libname}.pc
%{_libdir}/%{name}.so

%changelog
* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.2-0.1.20190816git8663c2e
- Initial SPEC release.

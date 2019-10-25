%global libname libQtOlm

%global commit0 f2d8e235a4af0625fdedaaf727fef5d51293bf1b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20190930

Name: libqtolm
Summary: A Qt wrapper for libolm
Version: 0
Release: 3.%{date}git%{shortcommit0}%{?dist}

License: GPLv3+
URL: https://gitlab.com/b0/libqtolm
Source0: %{url}/-/archive/%{commit0}.tar.gz/%{name}-%{shortcommit0}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Special Qt wrapper for libolm library.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0}
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
%license LICENSE
%{_libdir}/%{libname}.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/cmake/QtOlm
%{_libdir}/pkgconfig/QtOlm.pc
%{_libdir}/%{libname}.so

%changelog
* Fri Oct 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20190930gitf2d8e23
- Updated to latest Git snapshot.

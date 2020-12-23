%undefine __cmake_in_source_build
%global appname KQuickImageEditor
%global libname lib%{name}

Name: kquickimageeditor
Version: 0.1.2
Release: 1%{?dist}

License: LGPLv2+ and BSD and CC0
URL: https://invent.kde.org/libraries/%{name}
Summary: QtQuick components providing basic image editing capabilities

%global majmin %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

Source0: https://download.kde.org/%{stable}/%{name}/%{majmin}/%{name}-%{version}.tar.xz

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Quick)

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires: ninja-build

Requires: kf5-filesystem

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf5 -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*
%{_kf5_qmldir}/org/kde/%{name}/

%files devel
%{_kf5_libdir}/cmake/%{appname}/
%{_kf5_archdatadir}/mkspecs/modules/qt_%{appname}.pri

%changelog
* Wed Dec 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.2-1
- Initial SPEC release.

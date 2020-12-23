%undefine __cmake_in_source_build
%global framework kquickimageeditor
%global appname KQuickImageEditor
%global libname lib%{framework}

Name: kf5-%{framework}
Version: 0.1
Release: 1%{?dist}

License: LGPLv2+ and BSD and CC0
URL: https://invent.kde.org/libraries/%{framework}
Summary: QtQuick components providing basic image editing capabilities
Source0: https://download.kde.org/stable/%{framework}/%{version}/%{framework}-%{version}.tar.xz

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Quick)

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires: ninja-build

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{framework}-%{version} -p1
echo 'set_property(TARGET kquickimageeditorplugin PROPERTY SOVERSION 1)' >> src/CMakeLists.txt

%build
%cmake_kf5 -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*
%{_kf5_libdir}/%{libname}*.so.1*
%{_kf5_qmldir}/org/kde/%{framework}/

%files devel
%{_kf5_libdir}/cmake/%{appname}/
%{_kf5_libdir}/%{libname}*.so
%{_kf5_archdatadir}/mkspecs/modules/qt_%{appname}.pri

%changelog
* Wed Dec 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1-1
- Initial SPEC release.

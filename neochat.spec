%undefine __cmake_in_source_build

%global commit0 4dedb87efa46bd9bbdc4606d30772b3a189a3969
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20201122

Name: neochat
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and BSD
URL: https://invent.kde.org/network/%{name}
Summary: Client for matrix, the decentralized communication protocol
Source0: %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5QuickControls2)

BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Config)

BuildRequires: cmake(Quotient) >= 0.6.0
BuildRequires: pkgconfig(libcmark)

BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: kf5-rpm-macros
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

# Require exact version of Qt due to compiled QML usage.
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

Requires: hicolor-icon-theme
Requires: qt5-qtquickcontrols2%{?_isa}

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
%autosetup -n %{name}-%{commit0} -p1
sed -e 's/5.76.0/5.75.0/g' -i CMakeLists.txt

%build
%cmake_kf5 -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml
%{_kf5_datadir}/knotifications5/%{name}.notifyrc

%changelog
* Sun Nov 22 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20201122git4dedb87
- Initial SPEC release.

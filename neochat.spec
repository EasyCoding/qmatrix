%undefine __cmake_in_source_build

Name: neochat
Version: 1.1.1
Release: 1%{?dist}

License: GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and BSD
URL: https://invent.kde.org/network/%{name}
Summary: Client for matrix, the decentralized communication protocol
Source0: https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Widgets)

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5Notifications)

BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Quotient)
BuildRequires: pkgconfig(libcmark)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: ninja-build

Requires: hicolor-icon-theme
Requires: kf5-kirigami2%{?_isa}
Requires: kf5-kitemmodels%{?_isa}
Requires: kquickimageeditor%{?_isa}
Requires: qt5-qtquickcontrols2%{?_isa}

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
%autosetup -p1

%build
%cmake_kf5 -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml
%{_kf5_datadir}/knotifications5/%{name}.notifyrc

%changelog
* Tue Feb 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.1-1
- Updated to version 1.1.1.

* Tue Feb 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.0-1
- Updated to version 1.1.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.1-1
- Updated to version 1.0.1.

* Wed Dec 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-1
- Updated to version 1.0.

* Tue Dec 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-0.2.20201214git54b0773
- Updated to the latest Git snapshot.

* Mon Nov 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-0.1.20201123git5d4e787
- Initial SPEC release.

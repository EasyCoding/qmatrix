%global commit0 e56c41bb4d300c321cab9b28ef2e2a4b896409bb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20191015

Name: quaternion
Summary: Cross-platform desktop IM client for the Matrix protocol
Version: 0.0.9.4
Release: 0.1.%{date}git%{shortcommit0}%{?dist}

License: GPLv3+
URL: https://github.com/quotient-im/Quaternion
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

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

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libquotient-devel
BuildRequires: libolm-devel
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

Requires: hicolor-icon-theme

%description
Quaternion is a cross-platform desktop IM client for the Matrix
protocol in development.

%prep
%autosetup -n Quaternion-%{commit0} -p1
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGIT_SHA1=%{commit0} \
    -DUSE_INTREE_LIBQMC=OFF \
    ..
popd
%ninja_build -C %{_target_platform}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%ninja_install -C %{_target_platform}
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg*
%{_metainfodir}/*.appdata.xml

%changelog
* Wed Oct 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.0.9.4-0.1.20191015gite56c41b
- Updated to latest Git snapshot.

* Fri Nov 10 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.0.4-1.20171110git8502c54
- Updated to version 0.0.4 (snapshot).

* Sat Nov 04 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.0.1-4.20171103git3976b4d
- Updated to latest snapshot.

* Thu Oct 19 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.0.1-3.20171019git9cdc1bf
- Updated to latest snapshot.

* Wed Oct 18 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.0.1-2.20171017gite191260
- Updated to latest snapshot.

* Sun Sep 24 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170922gitdeeeaeb
- Initial SPEC release.

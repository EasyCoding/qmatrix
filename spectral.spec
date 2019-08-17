%global appname Spectral

%global commit0 3d8a3c7e36d0073a4a050e1a813b2ee3c61e34b3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20190817

# Git revision of SortFilterProxyModel...
%global commit1 770789ee484abf69c230cbf1b64f39823e79a181
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name: spectral
Summary: A glossy cross-platform Matrix client
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: GPLv3+
URL: https://gitlab.com/b0/%{name}
Source0: %{url}/-/archive/%{commit0}.tar.gz/%{name}-%{shortcommit0}.tar.gz
Source1: https://github.com/oKcerG/SortFilterProxyModel/archive/%{commit1}.tar.gz#/SortFilterProxyModel-%{shortcommit1}.tar.gz

BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libqtolm-devel
BuildRequires: libolm-devel
BuildRequires: cmark-devel
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

Provides: bundled(SortFilterProxyModel) = 0.1.1~git%{shortcommit1}
Requires: hicolor-icon-theme

%description
Spectral is a glossy cross-platform client for Matrix, the decentralized
communication protocol for instant messaging.

%prep
%autosetup -n %{name}-%{commit0}
mkdir -p %{_target_platform}

# Unpacking SortFilterProxyModel...
pushd include
    rm -rf SortFilterProxyModel
    tar -xf %{SOURCE1}
    mv SortFilterProxyModel-%{commit1} SortFilterProxyModel
popd

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGIT_SHA1=%{commit0} \
    ..
popd
%ninja_build -C %{_target_platform}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%ninja_install -C %{_target_platform}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.appdata.xml

%changelog
* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20190817git3d8a3c7
- Initial SPEC release.

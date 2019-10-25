%global appname Spectral

%global commit0 04bb4b1e98aa1a7064a5783d05428f0bf2d214d4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20191020

# Git revision of SortFilterProxyModel...
%global commit1 770789ee484abf69c230cbf1b64f39823e79a181
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name: spectral
Summary: A glossy cross-platform Matrix client
Version: 0
Release: 5.%{date}git%{shortcommit0}%{?dist}

License: GPLv3+
URL: https://gitlab.com/b0/%{name}
Source0: %{url}/-/archive/%{commit0}.tar.gz/%{name}-%{shortcommit0}.tar.gz
Source1: https://github.com/oKcerG/SortFilterProxyModel/archive/%{commit1}.tar.gz#/SortFilterProxyModel-%{shortcommit1}.tar.gz

# https://gitlab.com/b0/spectral/merge_requests/66
Patch0: spectral-qtquick2-linkage.patch

# https://gitlab.com/b0/spectral/merge_requests/67
Patch1: spectral-launcher-icon.patch

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
BuildRequires: cmake(Quotient) >= 0.6.0
BuildRequires: pkgconfig(libcmark)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

Provides: bundled(SortFilterProxyModel) = 0.1.1~git%{shortcommit1}
Requires: hicolor-icon-theme

Recommends: google-noto-emoji-color-fonts
Recommends: google-noto-emoji-fonts
Recommends: google-noto-sans-fonts
Recommends: google-roboto-fonts

%description
Spectral is a glossy cross-platform client for Matrix, the decentralized
communication protocol for instant messaging.

%prep
%autosetup -n %{name}-%{commit0} -p1
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
* Fri Oct 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-5.20191020git04bb4b1
- Updated to latest Git snapshot.

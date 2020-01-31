%global appname Spectral

%global commit0 6af7befd11322ee3029ce7faa5744d953a3e0948
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20200123

# Git revision of SortFilterProxyModel...
%global commit1 770789ee484abf69c230cbf1b64f39823e79a181
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name: spectral
Version: 0
Release: 7.%{date}git%{shortcommit0}%{?dist}

# Spectral - GPLv3+
# SortFilterProxyModel - MIT
License: GPLv3+ and MIT
URL: https://gitlab.com/spectral-im/%{name}
Summary: Glossy cross-platform Matrix client
Source0: %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1: https://github.com/oKcerG/SortFilterProxyModel/archive/%{commit1}/SortFilterProxyModel-%{shortcommit1}.tar.gz

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

# libquotient is not available on s390x.
ExcludeArch: s390x

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
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20200123git6af7bef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-6.20200123git6af7bef
- Updated to latest Git snapshot.

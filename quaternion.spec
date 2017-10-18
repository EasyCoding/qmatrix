%global commit0 e191260f12c00f1b1c086d5a951f38dcd72968b8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20171017

Summary: Cross-platform desktop IM client for the Matrix protocol
Name: quaternion
Version: 0.0.1
Release: 2.%{date}git%{shortcommit0}%{?dist}

License: GPLv3+
URL: https://github.com/QMatrixClient/Quaternion

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0: 0001-Unbundle-libqmatrixclient-library.patch

BuildRequires: libqmatrixclient-devel
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: qt5-qtbase-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Quaternion is a cross-platform desktop IM client for the Matrix
protocol in development.

%prep
%autosetup -n Quaternion-%{commit0} -p1

# Removing bundled library and using packaged version...
rm -rf lib
ln -s %{_includedir}/libqmatrixclient lib

%build
%cmake .
%make_build

%install
%make_install

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Wed Oct 18 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.0.1-2.20171017gite191260
- Updated to latest snapshot.

* Sun Sep 24 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170922gitdeeeaeb
- Initial SPEC release.

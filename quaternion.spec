%global commit0 deeeaebf414bde4fa9d372b6e2f052fa5a95102a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20170922

%global commit1 ae59271da3a199eb936aa709893ef592cd51f172
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Summary: Cross-platform desktop IM client for the Matrix protocol
Name: quaternion
Version: 0.0.1
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: GPLv3+
URL: https://github.com/QMatrixClient/Quaternion

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: https://github.com/QMatrixClient/libqmatrixclient/archive/%{commit0}.tar.gz#/libqmatrixclient-%{shortcommit1}.tar.gz

#BuildRequires: libqmatrixclient-devel
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

# Unpacking bundled libqmatrixclient...
rm -rf lib
tar -xf %{SOURCE1}
mv libqmatrixclient-%{commit1} lib

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
* Sun Sep 24 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170922gitdeeeaeb
- Initial SPEC release.

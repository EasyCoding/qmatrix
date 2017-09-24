%global commit0 deeeaebf414bde4fa9d372b6e2f052fa5a95102a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20170922

Summary: Cross-platform desktop IM client for the Matrix protocol
Name: quaternion
Version: 0.0.1
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: GPLv3+
URL: https://github.com/QMatrixClient/Quaternion

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: libqmatrixclient-devel
BuildRequires: qt5-qtquick1-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Quaternion is a cross-platform desktop IM client for the Matrix
protocol in development.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
%cmake .
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}

%changelog
* Sun Sep 24 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170922gitdeeeaeb
- Initial SPEC release.

%global commit0 ae59271da3a199eb936aa709893ef592cd51f172
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20170922

Summary: Qt-based library to make IM clients for the Matrix protocol
Name: libqmatrixclient
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: LGPL2.1
URL: https://github.com/QMatrixClient/%{name}

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
libqmatrixclient is a Qt-based library to make IM clients for the
Matrixprotocol. It is used by the Quaternion client and is a part
of the Quaternion project. The below instructions are the same for
Quaternion and libqmatrixclient (the source tree of Quaternion has
most up-to-date instructions but this source tree strives to closely
follow).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

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
%doc README.md CONTRIBUTING.md
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so

%changelog

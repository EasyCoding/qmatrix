%global sover 0.0.0

%global commit0 f2f85ba093df5dcd991fd206af4d79d57f4c7fc8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20171017

Summary: Qt-based library to make IM clients for the Matrix protocol
Name: libqmatrixclient
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: LGPLv2.1
URL: https://github.com/QMatrixClient/%{name}

Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: qt5-qtbase-devel
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
# Installing shared libraries...
mkdir -p "%{buildroot}%{_libdir}"
install -m 0755 -p %{name}.so.%{sover} "%{buildroot}%{_libdir}/%{name}.so.%{sover}"
ln -s %{name}.so.%{sover} "%{buildroot}%{_libdir}/%{name}.so.0"
ln -s %{name}.so.%{sover} "%{buildroot}%{_libdir}/%{name}.so"

# Installing additional development files...
mkdir -p "%{buildroot}%{_includedir}/%{name}/events"
mkdir -p "%{buildroot}%{_includedir}/%{name}/jobs/generated"
find . -maxdepth 1 -type f -name "*.h" -exec install -m 0644 -p '{}' %{buildroot}%{_includedir}/%{name} \;
find events -maxdepth 1 -type f -name "*.h" -exec install -m 0644 -p '{}' %{buildroot}%{_includedir}/%{name}/events \;
find jobs -maxdepth 1 -type f -name "*.h" -exec install -m 0644 -p '{}' %{buildroot}%{_includedir}/%{name}/jobs \;
find jobs/generated -maxdepth 1 -type f -name "*.h" -exec install -m 0644 -p '{}' %{buildroot}%{_includedir}/%{name}/jobs/generated \;

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
* Sun Sep 24 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170922gitae59271
- Initial SPEC release.

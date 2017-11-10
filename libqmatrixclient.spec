%global sover 0.1.0

%global commit0 92ede101bbde3b853a3eed20f6c097cd7a137b9c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20171110

Summary: Qt-based library to make IM clients for the Matrix protocol
Name: libqmatrixclient
Version: 0
Release: 5.%{date}git%{shortcommit0}%{?dist}

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
ln -s %{name}.so.%{sover} "%{buildroot}%{_libdir}/%{name}.so.0.1"
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
* Fri Nov 10 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-5.20171110git92ede10
- Updated to latest snapshot.

* Sat Nov 04 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-4.20171103git5bafd65
- Updated to latest snapshot.

* Fri Oct 20 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20171020git34faa56
- Updated to latest snapshot.

* Wed Oct 18 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.20171017gitf2f85ba
- Updated to latest snapshot.

* Sun Sep 24 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170922gitae59271
- Initial SPEC release.

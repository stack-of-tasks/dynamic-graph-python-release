%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-dynamic-graph-python
Version:        4.0.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS dynamic-graph-python package

License:        BSD
URL:            http://github.com/stack-of-tasks/dynamic-graph-python
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       ros-noetic-catkin
Requires:       ros-noetic-dynamic-graph
Requires:       ros-noetic-eigenpy
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  git
BuildRequires:  ros-noetic-dynamic-graph
BuildRequires:  ros-noetic-eigenpy
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Dynamic graph library Python bindings

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/noetic

%changelog
* Wed Mar 10 2021 Guilhem Saurel <guilhem.saurel@laas.fr> - 4.0.3-1
- Autogenerated by Bloom

* Mon Feb 22 2021 Guilhem Saurel <guilhem.saurel@laas.fr> - 4.0.2-3
- Autogenerated by Bloom

* Mon Feb 22 2021 Guilhem Saurel <guilhem.saurel@laas.fr> - 4.0.2-2
- Autogenerated by Bloom

* Tue Feb 09 2021 Guilhem Saurel <guilhem.saurel@laas.fr> - 4.0.2-1
- Autogenerated by Bloom

* Mon Nov 16 2020 Olivier Stasse <ostasse@laas.fr> - 4.0.1-1
- Autogenerated by Bloom

* Fri Nov 13 2020 Olivier Stasse <ostasse@laas.fr> - 4.0.0-1
- Autogenerated by Bloom

* Tue Jul 28 2020 Olivier Stasse <ostasse@laas.fr> - 3.5.3-2
- Autogenerated by Bloom


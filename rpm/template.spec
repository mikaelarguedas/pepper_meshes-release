Name:           ros-indigo-pepper-meshes
Version:        0.2.3
Release:        0%{?dist}
Summary:        ROS pepper_meshes package

Group:          Development/Libraries
License:        Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License
URL:            http://github.com/ros-naoqi/pepper_meshes/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  java-1.8.0-openjdk
BuildRequires:  ros-indigo-catkin

%description
meshes for the Aldebaran Robotics Pepper

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Feb 03 2016 Mikael Arguedas <mikael.arguedas@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Thu Jan 28 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Mon Jan 25 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.1-1
- Autogenerated by Bloom

* Wed Apr 08 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.1-0
- Autogenerated by Bloom


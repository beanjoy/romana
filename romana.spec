#
# Romana Spec File
#

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

#################################################################################
# common
#################################################################################
Name:		romana
Version: 	%{version}
Release: 	%{?revision}%{?dist}
Summary:	Calamari GUI front-end components
Requires: 	calamari-server
License: 	MIT
Group:   	System/Filesystems
URL:     	http://ceph.com/
Source0: 	%{name}_%{version}.tar.gz
%description
Contains the JavaScript GUI content for the Calamari frontend components
 (dashboard, login screens, administration screens)

%prep
echo "prep"

%install
echo "install"
mkdir -p %{buildroot}
cd %{buildroot}
tar xfz %{tarname}
cd %{name}-%{version}
for dir in manage admin login dashboard
do
mkdir -p ../opt/calamari/webapp/content/"$dir"
cp -pr "$dir"/dist/* ../opt/calamari/webapp/content/"$dir"/
done
cd ../
rm -rf /tmp/%{name}-%{version}
mv %{name}-%{version} /tmp/

%clean
echo "clean"
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files -n romana
/opt/calamari/webapp/content

%changelog

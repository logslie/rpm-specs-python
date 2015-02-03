%define module urllib3
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        1.10
Release:        1
Summary: 	Python HTTP library with thread-safe connection pooling and file post
License:        MIT
Group:          Development/Python
Url: 		http://urllib3.readthedocs.org/
Source:         https://pypi.python.org/packages/source/u/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python
Packager: 	Luis Martin Gil

%description
Python HTTP module with connection pooling and file POST abilities.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root %{buildroot} --install-purelib=%{python_sitelib} --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

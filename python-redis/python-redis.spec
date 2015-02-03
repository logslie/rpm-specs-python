%define module redis
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        2.10.3
Release:        1
Summary:        Python client for Redis key-value store
License:        MIT
Group:          Development/Python
Url:            http://github.com/andymccurdy/redis-py/
Source:         https://pypi.python.org/packages/source/r/redis/%{module}-%{version}.tar.gz
BuildRequires:  python
Vendor: 	Andy McCurdy <sedrik@gmail.com>
Packager: 	Luis Martin Gil

%description
Python client for Redis key-value store

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

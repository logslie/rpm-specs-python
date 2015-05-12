%define module tornado-redis
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        2.4.18
Release:        1
Summary:        Asynchronous Redis client for the Tornado Web Server.
License:        MIT
Group:          Development/Python
Url:            https://github.com/leporo/tornado-redis
Source:         https://pypi.python.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python
Vendor: 	Vlad Glushchuk
Packager: 	Laura Garcia Perez

%description
Asynchronous Redis client for the Tornado Web Server.

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

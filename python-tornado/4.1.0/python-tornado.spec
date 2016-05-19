%define module tornado
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        4.1.0
Release:        1
Summary:        Python web framework and asynchronous networking library
License:        MIT
Group:          Development/Python
Url:            https://github.com/tornadoweb/tornado
Source:         https://pypi.python.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python
Vendor: 	Facebook
Packager: 	Laura Garcia Perez
Requires:	python-backports-ssl_match_hostname
Requires:	python-pycurl

%description
Python web framework and asynchronous networking library

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

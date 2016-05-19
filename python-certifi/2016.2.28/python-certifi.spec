%define module certifi
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        2016.2.28
Release:        1
Summary:        Python package for providing Mozilla's CA Bundle.
License:        MIT
Group:          Development/Python
Url:            https://github.com/cython/backports_abc
Source:         https://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python
Vendor: 	Lukasa, kennethreitz
Packager: 	Laura Garcia Perez
Requires:	python-pycurl

%description
Python package for providing Mozilla's CA Bundle.

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

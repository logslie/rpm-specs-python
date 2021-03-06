%define module backports_abc
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        0.4
Release:        1
Summary:        A backport of recent additions to the 'collections.abc' module.
License:        MIT
Group:          Development/Python
Url:            https://github.com/cython/backports_abc
Source:         https://pypi.python.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python
Vendor: 	scoder
Packager: 	Laura Garcia Perez
Requires:	python-pycurl

%description
A backport of recent additions to the 'collections.abc' module.

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

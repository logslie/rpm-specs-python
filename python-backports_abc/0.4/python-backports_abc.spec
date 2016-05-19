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
Source:         https://pypi.python.org/packages/f5/d0/1d02695c0dd4f0cf01a35c03087c22338a4f72e24e2865791ebdb7a45eac/%{module}-%{version}.tar.gz\#md5=0b65a216ce9dc9c1a7e20a729dd7c05b
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

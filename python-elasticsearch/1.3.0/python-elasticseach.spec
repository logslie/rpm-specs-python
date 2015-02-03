%define module elasticsearch
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        1.3.0
Release:        1
Summary:        Official low-level client for Elasticsearch
License:        MIT
Group:          Development/Python
Url:            https://github.com/elasticsearch/elasticsearch-py
Source:         https://pypi.python.org/packages/source/e/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python
Packager: 	Luis Martin Gil
Requires:       python-urllib3 >= 1.8

%description
Official low-level client for Elasticsearch. Its goal is to provide common ground for all Elasticsearch-related code in Python; because of this it tries to be opinion-free and very extendable.

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

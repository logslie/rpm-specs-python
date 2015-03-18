%define module requests
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        2.6.0
Release:        1
Summary:        Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.
License:        Licensed under the Apache License, Version 2.0 
Group:          Development/Python
Url:            https://github.com/kennethreitz/requests
Source:         https://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python
Vendor: 	Kenneth Reitz
Packager: 	Luis Martin Gil

%description
Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.

Most existing Python modules for sending HTTP requests are extremely verbose and cumbersome. Python's builtin urllib2 module provides most of the HTTP capabilities you should need, but the api is thoroughly broken. It requires an enormous amount of work (even method overrides) to perform the simplest of tasks.

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

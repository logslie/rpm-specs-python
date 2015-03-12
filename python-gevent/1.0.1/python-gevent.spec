%define module gevent
%define _topdir %(echo $PWD)/
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define debug_package %{nil}

Name:           python-%module
Version:        1.0.1
Release:        1
Summary:        A coroutine-based Python networking library
License:        MIT
Group:          Development/Python
Url:            http://www.gevent.org/
Source:         https://pypi.python.org/packages/source/g/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  python
Vendor: 	Denis Bilenko <denis.bilenko@gmail.com>
Packager: 	Luis Martin Gil
BuildRequires:  glibc-devel
BuildRequires:  libevent-devel >= 1.4.0
BuildRequires:  python-devel
BuildRequires:  python-greenlet
Requires:       python-greenlet

%description
gevent is a coroutine-based Python networking library that uses greenlet to provide a high-level synchronous API on top of libevent event loop.

Features include:
	 
	 * convenient API around greenlets
         * familiar synchronization primitives (gevent.event, gevent.queue)
         * socket module that cooperates
         * WSGI server on top of libevent-http
         * DNS requests done through libevent-dns
         * monkey patching utility to get pure Python modules to cooperate

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

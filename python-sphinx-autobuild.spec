%define module sphinx-autobuild
%define oname sphinx_autobuild

# This package releases with different version tags on pypi than in its
# own repository release tags, internally the module uses the same versioning
# as on pypi, therefore we will use the Source0 using pypi instead of having
# two different version numbers here in the spec file.

Name:		python-sphinx-autobuild
Version:	2025.8.25
Release:	1
Summary:	Rebuild Sphinx documentation on changes, with hot reloading in the browser
License:	MIT
Group:		Development/Python
URL:		https://github.com/sphinx-doc/sphinx-autobuild
Source0:	https://files.pythonhosted.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
Rebuild Sphinx documentation on changes, with hot reloading in the browser.

%files
%doc README.rst
%{_bindir}/%{module}
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info

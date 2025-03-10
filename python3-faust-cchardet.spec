# TODO: system uchardet?
#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	cChardet - high speed universal character encoding detector
Summary(pl.UTF-8):	cChardet - szybki, uniwersalny wykrywacz kodowania znaków
Name:		python3-faust-cchardet
Version:	2.1.19
Release:	2
License:	MPL v1.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/faust-cchardet/
Source0:	https://files.pythonhosted.org/packages/source/f/faust-cchardet/faust-cchardet-%{version}.tar.gz
# Source0-md5:	f67b9cb0198284535b062992cb47be40
URL:		https://pypi.org/project/faust-cchardet/
BuildRequires:	libstdc++-devel
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-pkgconfig
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
Obsoletes:	python3-cchardet < 2.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cChardet is high speed universal character encoding detector - binding
to uchardet.

%description -l pl.UTF-8
cChardet to szybki, uniwersalny wykrywacz kodowania znaków - wiązanie
do biblioteki uchardet.

%prep
%setup -q -n faust-cchardet-%{version}

%build
%py3_build

%if %{with tests}
LC_ALL=C \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} -m pytest src/tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%attr(755,root,root) %{_bindir}/cchardetect
%dir %{py3_sitedir}/cchardet
%{py3_sitedir}/cchardet/*.py
%attr(755,root,root) %{py3_sitedir}/cchardet/*.so
%{py3_sitedir}/cchardet/__pycache__
%{py3_sitedir}/faust_cchardet-%{version}-py*.egg-info

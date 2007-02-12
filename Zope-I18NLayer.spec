%define		zope_subname	I18NLayer
Summary:	Provide multilanguage content support for existing document types
Summary(pl.UTF-8):   Umożliwia tworzenie wielojęzykowych dokumentów w środowisku Zope
Name:		Zope-%{zope_subname}
Version:	0.6.0
Release:	1
License:	GPL v2+
Group:		Development/Tools
#Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
Source0:	http://dl.sourceforge.net/collective/I18NLayer-%{version}.tar.gz
# Source0-md5:	63097d2b464724c381afd3d598233994
URL:		http://plone.org/Members/longsleep/I18NLayer/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMFPlone
Requires:	Zope-PloneLanguageTool
Requires:	Zope-archetypes

Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I18NLayer provides a transparent overlay above multiple content
objects to provide multilanguage content support for existing document
types.

%description -l pl.UTF-8
I18NLayer dostarcza mechanizm tworzenia wielojęzykowych dokumentów dla
produktów Zope.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,i18n,skins,tests,*.py,version.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{_datadir}/%{name}

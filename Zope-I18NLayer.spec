%define		zope_subname	I18NLayer
Summary:	Provide multilanguage content support for existing document types
Summary(pl):	Umo¿liwia tworzenie wielojêzykowych dokumentów w ¶rodowisku Zope
Name:		Zope-%{zope_subname}
Version:	0.5.7
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	7912fd7590e084a838b445c91b616fb8
URL:		http://plone.org/Members/longsleep/I18NLayer/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMFPlone
Requires:	Zope-archetypes
Requires:	Zope-PloneLanguageTool

Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I18NLayer provides a transparent overlay above multiple content
objects to provide multilanguage content support for existing document
types.

%description -l pl
I18NLayer dostarcza mechanizm tworzenia wielojêzykowych dokumentów dla
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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{_datadir}/%{name}

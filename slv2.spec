Summary:	LV2 host library to make LV2 plugin use as simple as possible
Summary(pl.UTF-8):	Biblioteka hosta LV2 ułatwiająca korzystanie z wtyczek LV2
Name:		slv2
Version:	0.6.6
Release:	5
License:	GPL v2+
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	b8e8e0e82dd04324fcd533e8acd1ce85
Patch0:		link.patch
URL:		http://drobilla.net/software/slv2/
BuildRequires:	doxygen
BuildRequires:	jack-audio-connection-kit-devel >= 0.107.0
BuildRequires:	libraptor2-devel >= 2.0
BuildRequires:	lv2core-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	redland-devel >= 1.0.13
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLV2 is a library to make the use of LV2 plugins as simple as possible
for applications. It is written in standard C using the Redland RDF
toolkit. The Data (RDF) and code (shared library) functionality in
SLV2 is strictly separated so it is simple to control where each is
used (e.g. it is possible to discover/investigate plugins and related
data without loading any shared libraries, avoiding the associated
risks)

%description -l pl.UTF-8
SLV2 to biblioteka ułatwiająca korzystanie z wtyczek LV2 w
aplikacjach. Jest napisana w standardowym C z wykorzystaniem
biblioteki Redland RDF. Dane (RDF) i kod (biblioteka współdzielona) są
w SLV2 ściśle oddzielone, dzięki czemu łatwo kontrolować, kiedy które
z nich jest używane (np. możliwe jest wykrywanie wtyczek i powiązanych
z nimi danych bez ładowania żadnych bibliotek współdzielonych).

%package devel
Summary:	Header files for SLV2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SLV2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraptor2-devel >= 2.0
Requires:	redland-devel >= 1.0.13
Requires:	lv2core-devel >= 1.0

%description devel
Header files for SLV2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SLV2.

%package utils
Summary:	LV2 utilities
Summary(pl.UTF-8):	Narzędzia LV2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description utils
LV2 utilities.

%description utils -l pl.UTF-8
Narzędzia LV2.

%package apidocs
Summary:	SLV2 API documentation
Summary(pl.UTF-8):	Dokumentacja API SLV2
Group:		Documentation

%description apidocs
Documetation for SLV2 API in HTML format.

%description apidocs -l pl.UTF-8
Dokumentacja API SLV2 w formacie HTML.

%prep
%setup -q
%patch0 -p1
sed -i 's|/lib/|/%{_lib}/|g' src/world.c
sed -i "s|/lib'|/%{_lib}'|" autowaf.py

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--htmldir=%{_docdir}/%{name}-apidocs-%{version} \
	--build-docs \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

# let rpm generate .so deps
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libslv2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libslv2.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libslv2.so
%{_includedir}/slv2
%{_pkgconfigdir}/slv2.pc
%{_mandir}/man3/slv2*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lv2_*
%{_mandir}/man1/lv2_*.1*

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/%{name}-apidocs-%{version}

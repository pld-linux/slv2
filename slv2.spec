Summary:	LV2 host library
Summary(pl.UTF-8):	Biblioteka LV2
Name:		slv2
Version:	0.6.6
Release:	0.2
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	b8e8e0e82dd04324fcd533e8acd1ce85
URL:		http://drobilla.net/software/slv2
BuildRequires:	doxygen
BuildRequires:	python
BuildRequires:	lv2core-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	redland-devel >= 1.0.6
BuildRequires:	jack-audio-connection-kit-devel >= 0.107.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A host library to make LV2 plugin use as simple as possible.

SLV2 is a library to make the use of LV2 plugins as simple as possible for 
applications. It is written in standard C using the Redland RDF toolkit. The 
Data (RDF) and code (shared library) functionality in SLV2 is strictly
separated so it is simple to control where each is used (e.g. it is possible
to discover/investigate plugins and related data without loading any shared 
libraries, avoiding the associated risks)

%package devel
Summary:	Header files for lv2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lv2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for lv2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lv2.

%package utils
Summary:	Utils for lv2
Summary(pl.UTF-8):	Narzędzia lv2
Group:		Applications/Sound

%description utils
Utils for lv2.

%description utils -l pl.UTF-8
Narzędzia lv2.

%package apidocs
Summary:	Lv2 API documentation
Summary(pl.UTF-8):	Dokumentacja API lv2
Group:		Documentation

%description apidocs
Documetation for lv2 API in HTML format.

%description apidocs -l pl.UTF-8
Dokumentacja API lv2 w formacie HTML.

%prep
%setup -q
sed -i 's|/lib/|/%{_lib}/|g' src/world.c
sed -i "s|/lib'|/%{_lib}'|" autowaf.py

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}/ \
	--htmldir=%{_docdir}/%{name}-apidocs-%{version} \
	--build-docs \
	--strict
./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libslv2.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/slv2
%{_libdir}/libslv2.so
%{_pkgconfigdir}/slv2.pc
%{_mandir}/man3/slv2*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/lv2_*

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/%{name}-apidocs-%{version}

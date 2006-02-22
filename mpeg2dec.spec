Summary:	MPEG-2 Decoder
Summary(pl):	Dekoder plików MPEG-2
Name:		mpeg2dec
Version:	0.4.0b
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://libmpeg2.sourceforge.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	52d10ea80595ec83d8557ba7ac6dc8e6
Patch0:		%{name}-opt.patch
Patch1:		%{name}-use_pic.patch
URL:		http://libmpeg2.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
%ifarch ppc
# version with altivec support (almost?) fixed
BuildRequires:	gcc >= 5:3.3.2-3
%endif
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
Requires:	%{name}-lib = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MPEG-2 Decoder.

%description -l pl
Dekoder MPEG-2.

%package lib
Summary:	MPEG-2 Decoder library
Summary(pl):	Biblioteka dekoduj±ca pliki MPEG-2
Group:		Libraries

%description lib
MPEG-2 Decoder library and extract_mpeg2 utility.

%description lib -l pl
Biblioteka dekoduj±ca pliki MPEG-2 i narzêdzie extract_mpeg2.

%package devel
Summary:	MPEG-2 Decoder development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych dekodera MPEG-2
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXv-devel

%description devel
MPEG-2 Decoder development files.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych dekodera MPEG-2.

%package static
Summary:	MPEG-2 Decoder static libraries
Summary(pl):	Statyczne biblioteki dekodera MPEG-2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
MPEG-2 Decoder static libraries.

%description static -l pl
Statyczne biblioteki dekodera MPEG-2.

%prep
%setup -q -n %{name}-0.4.0
%patch0 -p1
%patch1 -p1

# using altivec code w/o altivec ABI (still) triggers gcc 3.3.2 ICE
# but I suppose it's needed for this code anyway
%{__perl} -pi -e 's/-maltivec/-maltivec -mabi=altivec/' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?debug:--enable-debug} \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeg2dec
%{_mandir}/man1/mpeg2dec.1*

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/corrupt_mpeg2
%attr(755,root,root) %{_bindir}/extract_mpeg2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/extract_mpeg2.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/mpeg2dec
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

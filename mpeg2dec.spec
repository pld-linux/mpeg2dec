Summary:	MPEG-2 Decoder
Summary(pl):	Dekoder plików MPEG-2
Name:		mpeg2dec
Version:	0.2.0
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.linuxvideo.org/mpeg2dec/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
URL:		http://www.linuxvideo.org/mpeg2dec/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
MPEG-2 Decoder.

%description -l pl
Dekoder MPEG-2.

%package devel
Summary:	MPEG-2 Decoder development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych dekodera MPEG-2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
MPEG-2 Decoder development files.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych dekodera MPEG-2.

%package static
Summary:	MPEG-2 Decoder static libraries
Summary(pl):	Statyczne biblioteki dekodera MPEG-2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
MPEG-2 Decoder static libraries.

%description static -l pl
Statyczne biblioteki dekodera MPEG-2.

%prep
%setup -q
%patch -p1

%build
libtoolize --copy --force
aclocal
%{__autoconf}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/mpeg2dec
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

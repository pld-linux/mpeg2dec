Summary:	MPEG-2 Decoder
Summary(pl):	Dekoder plików MPEG-2
Name:		mpeg2dec
Version:	0.2.0
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.linuxvideo.org/mpeg2dec/files/%{name}-%{version}.tar.gz
URL:		http://www.linuxvideo.org/mpeg2dec/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	arts-devel
BuildRequires:	esound-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
MPEG-2 Decoder.

%description -l pl
Dekoder MPEG-2.

%package devel
Summary:	MPEG-2 Decoder development files
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
MPEG-2 Decoder development files

%package static
Summary:	MPEG-2 Decoder static libraries
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
MPEG-2 Decoder static libraries.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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

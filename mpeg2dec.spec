Summary:	MPEG-2 Decoder
Summary(pl):	Dekoder plików MPEG-2
Name:		mpeg2dec
Version:	0.2.0
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
URL:		http://www.linuxvideo.org/
Source0:	ftp://www.linuxvideo.org/mpeg2dec/files/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
MPEG-2 Decoder

%description -l pl
Dekoder MPEG-2

%package devel
Summary:	MPEG-2 Decoder development files
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika

%description devel
MPEG-2 Decoder development files

%package static
Summary:	MPEG-2 Decoder static libraries
Group:		X11/Libraries
Group(de):	X11/libraries
Group(pl):	X11/Biblioteki

%description static
MPEG-2 Decoder static libraries
 
%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.la
%{_libdir}/*.a

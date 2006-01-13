%define		CVSSNAPSHOT	20060112

Summary:	A cross-platform serial port class
Summary(pl):	Wieloplatformowa klasa do obs³ugi portu szeregowego
Name:		qextserialport
Version:	1.0.0
Release:	0.1_%{CVSSNAPSHOT}
License:	GPL
Group:		X11/Libraries
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/qextserialport login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/qextserialport \
# 	co -P qextserialport
Source0:	qextserialport.tgz
URL:		http://qextserialport.sf.net/
BuildRequires:	QtCore
Requires:	QtCore
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QextSerialPort is a cross-platform serial port class. This class
encapsulates a serial port on both POSIX and Windows systems.

%description -l pl
QextSerialPort to wieloplatformowa klasa do obs³ugi portu szeregowego.
Obudowuje obs³ugê portu szeregowego na systemach zgodnych z POSIX oraz
Windows.

%package devel
Summary:	QextSerialPort development files
Summary(pl):	Pliki programistyczne QextSerialPort
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
QextSerialPort development files.

%description devel -l pl
Pliki programistyczne QextSerialPort.

%prep
%setup -q -n %{name}

%build
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}
install -d $RPM_BUILD_ROOT%{_libdir}

install build/libqextserialport* $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqextserialport*.so.*

%files devel
%defattr(644,root,root,755)
%doc html
%attr(755,root,root) %{_libdir}/libqextserialport.so
%{_includedir}/*

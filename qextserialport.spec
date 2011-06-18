%define		CVSSNAPSHOT	20060112

Summary:	A cross-platform serial port class
Summary(pl.UTF-8):	Wieloplatformowa klasa do obsługi portu szeregowego
Name:		qextserialport
Version:	1.0.0
Release:	0.2_%{CVSSNAPSHOT}
License:	GPL
Group:		Libraries
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/qextserialport login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/qextserialport \
# 	co -P qextserialport
Source0:	%{name}.tgz
# Source0-md5:	4ce794658c5467d06266417bcdd0ca2a
URL:		http://qextserialport.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QextSerialPort is a cross-platform serial port class. This class
encapsulates a serial port on both POSIX and Windows systems.

%description -l pl.UTF-8
QextSerialPort to wieloplatformowa klasa do obsługi portu szeregowego.
Obudowuje obsługę portu szeregowego na systemach zgodnych z POSIX oraz
Windows.

%package devel
Summary:	QextSerialPort development files
Summary(pl.UTF-8):	Pliki programistyczne QextSerialPort
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel

%description devel
QextSerialPort development files.

%description devel -l pl.UTF-8
Pliki programistyczne QextSerialPort.

%prep
%setup -q -n %{name}

find . -type d -name CVS | xargs rm -r

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}
install -d $RPM_BUILD_ROOT%{_libdir}

cp -a build/libqextserialport.so* $RPM_BUILD_ROOT%{_libdir}
install [!w]*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqextserialport.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libqextserialport.so.1

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_libdir}/libqextserialport.so
%{_includedir}/posix_qextserialport.h
%{_includedir}/qextserialbase.h
%{_includedir}/qextserialport.h

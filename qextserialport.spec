%define		CVSSNAPSHOT	20060112

Summary:	A cross-platform serial port class.
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

#%define		_noautoreqdep	libGL.so.1 libGLU.so.1
#%define         _noautostrip    '.*_debug\\.so*'

%description
QextSerialPort is a cross-platform serial port class. This class
encapsulates a serial port on both POSIX and Windows systems.

%package devel
Summary:	QextSerialPort development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
QextSerialPort development files

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
%attr(640,root,root)
%attr(755,root,root) %{_libdir}/libqextserialport*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqextserialport.so
%doc html
%{_includedir}/*

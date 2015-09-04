%define		kdeframever	5.13
%define		qtver		5.3.2
%define		kfname		kemoticons

Summary:	Convert text emoticons to graphical emoticons
Name:		kf5-%{kfname}
Version:	5.13.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	00507676a628255bd76d3ed418eafc91
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KEmoticons converts emoticons from text to a graphical representation
with images in HTML. It supports setting different themes for
emoticons coming from different providers.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %ghost %{_libdir}/libKF5Emoticons.so.5
%attr(755,root,root) %{_libdir}/libKF5Emoticons.so.*.*
%dir %{qt5dir}/plugins/kf5/emoticonsthemes
%attr(755,root,root) %{qt5dir}/plugins/kf5/KEmoticonsIntegrationPlugin.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/emoticonsthemes/adium.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/emoticonsthemes/kde.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/emoticonsthemes/pidgin.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/emoticonsthemes/xmpp.so
%{_datadir}/kservices5/emoticonstheme_adium.desktop
%{_datadir}/kservices5/emoticonstheme_kde.desktop
%{_datadir}/kservices5/emoticonstheme_pidgin.desktop
%{_datadir}/kservices5/emoticonstheme_xmpp.desktop
%{_datadir}/kservicetypes5/kemoticonsTheme.desktop
%{_datadir}/emoticons/Breeze
%{_datadir}/emoticons/Glass

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KEmoticons
%{_includedir}/KF5/kemoticons_version.h
%{_libdir}/cmake/KF5Emoticons
%attr(755,root,root) %{_libdir}/libKF5Emoticons.so
%{qt5dir}/mkspecs/modules/qt_KEmoticons.pri

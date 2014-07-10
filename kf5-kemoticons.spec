# TODO:
# Not packaged:
# /usr/include/KF5
# /usr/lib/qt5/plugins/kf5/emoticonsthemes
# /usr/share/emoticons/Glass
# /usr/share/kservices5
# /usr/share/kservicetypes5

%define         _state          stable
%define		orgname		kemoticons

Summary:	Convert text emoticons to graphical emoticons
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	27adb273827ff6abc8dd8d3983765bca
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
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
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	-D_IMPORT_PREFIX=%{_prefix} \
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
%attr(755,root,root) %{_libdir}/libKF5Emoticons.so.5.0.0
%dir %{qt5dir}/plugins/kf5/emoticonsthemes
%attr(755,root,root) %{qt5dir}/plugins/kf5/emoticonsthemes/adium.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/emoticonsthemes/kde.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/emoticonsthemes/pidgin.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/emoticonsthemes/xmpp.so
%{_datadir}/kservices5/emoticonstheme_adium.desktop
%{_datadir}/kservices5/emoticonstheme_kde.desktop
%{_datadir}/kservices5/emoticonstheme_pidgin.desktop
%{_datadir}/kservices5/emoticonstheme_xmpp.desktop
%{_datadir}/kservicetypes5/kemoticonsTheme.desktop
%{_datadir}/emoticons/Glass/angry.png
%{_datadir}/emoticons/Glass/bat.png
%{_datadir}/emoticons/Glass/beer.png
%{_datadir}/emoticons/Glass/biggrin.png
%{_datadir}/emoticons/Glass/cake.png
%{_datadir}/emoticons/Glass/camera.png
%{_datadir}/emoticons/Glass/cat.png
%{_datadir}/emoticons/Glass/clock.png
%{_datadir}/emoticons/Glass/cocktail.png
%{_datadir}/emoticons/Glass/confused.png
%{_datadir}/emoticons/Glass/cry.png
%{_datadir}/emoticons/Glass/cup.png
%{_datadir}/emoticons/Glass/dog.png
%{_datadir}/emoticons/Glass/email.png
%{_datadir}/emoticons/Glass/embarassed.png
%{_datadir}/emoticons/Glass/emoticons.xml
%{_datadir}/emoticons/Glass/film.png
%{_datadir}/emoticons/Glass/foot_in_mouth.png
%{_datadir}/emoticons/Glass/innocent.png
%{_datadir}/emoticons/Glass/kiss.png
%{_datadir}/emoticons/Glass/lightbulb.png
%{_datadir}/emoticons/Glass/love.png
%{_datadir}/emoticons/Glass/note.png
%{_datadir}/emoticons/Glass/oh.png
%{_datadir}/emoticons/Glass/omg.png
%{_datadir}/emoticons/Glass/phone.png
%{_datadir}/emoticons/Glass/present.png
%{_datadir}/emoticons/Glass/rose.png
%{_datadir}/emoticons/Glass/sad.png
%{_datadir}/emoticons/Glass/shade.png
%{_datadir}/emoticons/Glass/sleep.png
%{_datadir}/emoticons/Glass/smile.png
%{_datadir}/emoticons/Glass/star.png
%{_datadir}/emoticons/Glass/teeth.png
%{_datadir}/emoticons/Glass/thumbs_down.png
%{_datadir}/emoticons/Glass/thumbs_up.png
%{_datadir}/emoticons/Glass/tongue.png
%{_datadir}/emoticons/Glass/undecided.png
%{_datadir}/emoticons/Glass/unhappy.png
%{_datadir}/emoticons/Glass/unlove.png
%{_datadir}/emoticons/Glass/wilted_rose.png
%{_datadir}/emoticons/Glass/wink.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KEmoticons
%{_includedir}/KF5/kemoticons_version.h
%{_libdir}/cmake/KF5Emoticons
%attr(755,root,root) %{_libdir}/libKF5Emoticons.so
%{qt5dir}/mkspecs/modules/qt_KEmoticons.pri

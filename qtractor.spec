#define debug_package          %{nil}
%define _empty_manifest_terminate_build 0

Name:       qtractor
Version:    0.9.38
Release:    1
Summary:    An Audio/MIDI multi-track sequencer
License:    GPLv2+
Group:      Sound
Source0:    http://softlayer-dal.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
URL:        http://qtractor.sourceforge.net/

BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(aubio)
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(suil-0)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  desktop-file-utils
BuildRequires:  qmake5
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:	qt6-qtbase-theme-gtk3

Requires:       dssi
Requires:       ladspa


%description
Qtractor is an Audio/MIDI multi-track sequencer application
written in C++ around the Qt4 toolkit using Qt Designer.

The initial target platform will be Linux, where the Jack Audio
Connection Kit (JACK) for audio, and the Advanced Linux Sound
Architecture (ALSA) for MIDI, are the main infrastructures to
evolve as a fairly-featured Linux Desktop Audio Workstation GUI,
specially dedicated to the personal home-studio.

%prep
%autosetup -p1

%build
%cmake \
        -DCONFIG_QT6=yes \
        -DCONFIG_LIBSUIL=yes

%make_build

%install
%make_install -C build

# Fix the .desktop file by removing
# 2 non-Mdv key and 2 non-standard categories
desktop-file-install \
    --remove-key="X-SuSE-translate" \
    --remove-key="Version" \
    --remove-category="MIDI" \
    --remove-category="ALSA" \
    --remove-category="JACK" \
    --add-category="Midi" \
    --add-category="X-MandrivaLinux-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/org.rncbc.qtractor.desktop
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc ChangeLog README
%{_bindir}/%{name}
%{_libdir}/qtractor/qtractor_plugin_scan
%{_datadir}/applications/org.rncbc.qtractor.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.qtractor.svg
%{_datadir}/icons/hicolor/32x32/apps/org.rncbc.qtractor.png
%{_datadir}/icons/hicolor/32x32/mimetypes/*.png
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/org.rncbc.qtractor.xml
%{_datadir}/metainfo/org.rncbc.qtractor.metainfo.xml
%{_datadir}qtractor/audio/metro_bar.wav
%{_datadir}qtractor/audio/metro_beat.wav
%{_mandir}/man1/*
%{_mandir}/fr/man1/qtractor.1.*

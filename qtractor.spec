%define debug_package          %{nil}

Name:       qtractor
Version:    0.9.12
Release:    1
Summary:    An Audio/MIDI multi-track sequencer
License:    GPLv2+
Group:      Sound
Source0:    http://softlayer-dal.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
URL:        http://qtractor.sourceforge.net/
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(suil-0)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  desktop-file-utils
BuildRequires:  qmake5
BuildRequires:  cmake(Qt5LinguistTools)

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
%configure

%make_build

%install
%make_install

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
%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%{name}
%{_libdir}/qtractor/qtractor_plugin_scan
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/32x32/mimetypes/*.png
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/qtractor.appdata.xml
%{_mandir}/man1/*

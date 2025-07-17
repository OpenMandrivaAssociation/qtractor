Summary:		An Audio/MIDI multi-track sequencer
Name:	qtractor

Version:		1.5.6
Release:		1
License:		GPLv2+
Group:	Sound
Url:		https://qtractor.sourceforge.net/
Source0:	https://sourceforge.net/projects/qtractor/files/qtractor/%{version}/%{name}-%{version}.tar.gz
BuildRequires:		cmake >= 3.17
BuildRequires:		desktop-file-utils
BuildRequires:		git
BuildRequires:		qmake-qt6
BuildRequires:		qt6-qtbase-theme-gtk3
BuildRequires:		cmake(Qt6)
BuildRequires:		cmake(Qt6Core) >= 6.9
BuildRequires:		cmake(Qt6LinguistTools)
BuildRequires:		cmake(Qt6Svg)
BuildRequires:		cmake(Qt6Widgets)
BuildRequires:		cmake(Qt6Xml)
BuildRequires:		clap-devel
BuildRequires:		ladspa-devel
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(aubio)
BuildRequires:		pkgconfig(dssi)
BuildRequires:		pkgconfig(gtk+-2.0)
BuildRequires:		pkgconfig(gtkmm-2.4)
BuildRequires:		pkgconfig(jack)
BuildRequires:		pkgconfig(liblo)
BuildRequires:		pkgconfig(lilv-0)
BuildRequires:		pkgconfig(lv2)
BuildRequires:		pkgconfig(mad)
BuildRequires:		pkgconfig(ogg)
BuildRequires:		pkgconfig(rubberband)
BuildRequires:		pkgconfig(samplerate)
BuildRequires:		pkgconfig(sndfile)
BuildRequires:		pkgconfig(suil-0)
BuildRequires:		pkgconfig(vorbis)
BuildRequires:		pkgconfig(vst3sdk)
BuildRequires:		pkgconfig(vulkan)
BuildRequires:		pkgconfig(xcb)
BuildRequires:		pkgconfig(xkbcommon-x11)
BuildRequires:		pkgconfig(zlib)
Requires:	dssi
Requires:	ladspa

%description
Qtractor is an Audio/MIDI multi-track sequencer application written in C++
around the Qt toolkit using Qt Designer.
The initial target platform will be Linux, where the Jack Audio Connection Kit
(JACK) for audio, and the Advanced Linux Sound Architecture (ALSA) for MIDI,
are the main infrastructures to evolve as a fairly-featured Linux Desktop
Audio Workstation GUI, specially dedicated to the personal home-studio.

%files -f %{name}.lang
%doc ChangeLog README README.*
%{_bindir}/%{name}
%{_libdir}/%{name}/%{name}_plugin_scan
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_datadir}/icons/hicolor/32x32/apps/org.rncbc.%{name}.png
%{_datadir}/icons/hicolor/32x32/mimetypes/*.png
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/org.rncbc.%{name}.xml
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_datadir}/%{name}/audio/metro_bar.wav
%{_datadir}/%{name}/audio/metro_beat.wav
%{_datadir}/%{name}/instruments/Standard1.ins
%{_datadir}/%{name}/palette/
%{_mandir}/man1/%{name}.1.*
%{_mandir}/fr/man1/%{name}.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake \
	-DCONFIG_QT6=yes \
%ifarch aarch64
	-DCONFIG_SSE=no \
%else
	-DCONFIG_SSE=yes	 \
%endif
	-DCONFIG_VST3=yes \
	-DCONFIG_CLAP=yes \
	-DCONFIG_WAYLAND=no

%make_build


%install
%make_install -C build

# Fix the .desktop file by removing
# 2 non-Mdv key and 2 non-standard categories
desktop-file-edit \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--remove-category="MIDI" \
	--remove-category="ALSA" \
	--remove-category="JACK" \
	--add-category="Midi" \
	--add-category="X-MandrivaLinux-Sound" \
	%{buildroot}%{_datadir}/applications/org.rncbc.%{name}.desktop

%find_lang %{name} --with-qt

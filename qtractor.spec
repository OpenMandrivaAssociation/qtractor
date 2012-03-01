Name:       qtractor
Version:    0.5.4
Release:    1
Summary:    An Audio/MIDI multi-track sequencer
License:    GPLv2+
Group:      Sound
Source0:    %{name}-%{version}.tar.gz
URL:        http://qtractor.sourceforge.net/
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  qt4-devel
BuildRequires:  jackit-devel
BuildRequires:  libalsa-devel
BuildRequires:  sndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  mad-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  rubberband-devel
BuildRequires:  liblo-devel
BuildRequires:  ladspa-devel
BuildRequires:  dssi-devel
BuildRequires:  lilv-devel suil-devel
BuildRequires:  slv2-devel
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils

Requires:       dssi ladspa
Requires:       suil-gtk2-in-qt4

%description
Qtractor is an Audio/MIDI multi-track sequencer application
written in C++ around the Qt4 toolkit using Qt Designer.

The initial target platform will be Linux, where the Jack Audio
Connection Kit (JACK) for audio, and the Advanced Linux Sound
Architecture (ALSA) for MIDI, are the main infrastructures to
evolve as a fairly-featured Linux Desktop Audio Workstation GUI,
specially dedicated to the personal home-studio.

%prep
%setup

%build
%configure --enable-lilv --enable-suil --localedir=%{_localedir}/%{name}

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=%{buildroot}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_localedir}/%{name}/*.qm

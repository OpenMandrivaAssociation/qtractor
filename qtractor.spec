%define name qtractor
%define version 0.4.5
%define release %mkrel 2

Summary: 	An Audio/MIDI multi-track sequencer
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPLv2+
Group:		Sound
Source0:	%{name}-%{version}.tar.gz
URL:		http://qtractor.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  qt4-devel	
BuildRequires:	jackit-devel >= 0.100.0
BuildRequires:	libalsa-devel
BuildRequires:	sndfile-devel >= 1.0.11
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	rubberband-devel
BuildRequires:	liblo-devel
BuildRequires:	ladspa-devel
BuildRequires:	dssi-devel
BuildRequires:  slv2-devel lv2core-devel 

Requires:		raptor redland rasqal dssi lv2core ladspa

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
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

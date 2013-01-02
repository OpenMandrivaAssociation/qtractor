%define debug_package          %{nil}

Name:       qtractor
Version:    0.5.7
Release:    1
Summary:    An Audio/MIDI multi-track sequencer
License:    GPLv2+
Group:      Sound
Source0:    %{name}-%{version}.tar.gz
URL:        http://qtractor.sourceforge.net/
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
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils

Requires:       dssi ladspa
Requires:       suil-gtk2-in-qt4
Requires:       suil-x11-in-qt4

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

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/mimetypes/*.png
%{_datadir}/mime/packages/%{name}.xml
%{_localedir}/%{name}/*.qm


%changelog
* Sat Jun 16 2012 Frank Kober <emuse@mandriva.org> 0.5.5-1
+ Revision: 806016
- new version 0.5.5

* Tue Apr 24 2012 Frank Kober <emuse@mandriva.org> 0.5.4-2
+ Revision: 793158
- rebuild for new suil and lilv

* Thu Mar 01 2012 Frank Kober <emuse@mandriva.org> 0.5.4-1
+ Revision: 781661
- new version 0.5.4

* Wed Dec 28 2011 Frank Kober <emuse@mandriva.org> 0.5.3-1
+ Revision: 746188
- new version 0.5.3

* Thu Dec 22 2011 Frank Kober <emuse@mandriva.org> 0.5.2-2
+ Revision: 744383
- rebuild to enable Jack Session with jack 1.9.8

* Sat Dec 17 2011 Frank Kober <emuse@mandriva.org> 0.5.2-1
+ Revision: 743204
- new version 0.5.2
  o localedir configure option added
  o mkrel macro removed

* Sun Oct 23 2011 Frank Kober <emuse@mandriva.org> 0.5.1-1
+ Revision: 705769
- new version 0.5.1
  o fix for new locale path in Makefile.in added

* Sun Oct 02 2011 Frank Kober <emuse@mandriva.org> 0.5.0-2
+ Revision: 702432
- rebuild (broken gtk symbol)

* Sat Aug 06 2011 Frank Kober <emuse@mandriva.org> 0.5.0-1
+ Revision: 693394
- new version 0.5.0

* Mon Jun 27 2011 Frank Kober <emuse@mandriva.org> 0.4.9-4
+ Revision: 687553
- enable new LV2 GUI support through suil and lilv

* Tue Jun 21 2011 Frank Kober <emuse@mandriva.org> 0.4.9-3
+ Revision: 686551
+ rebuild (emptylog)

* Tue Jun 21 2011 Frank Kober <emuse@mandriva.org> 0.4.9-2
+ Revision: 686516
- rebuild to enable LV2 GTK UI Support

* Thu May 26 2011 Frank Kober <emuse@mandriva.org> 0.4.9-1
+ Revision: 679219
- new version 0.4.9 (source sync)
- new version 0.4.9

* Mon Apr 18 2011 Frank Kober <emuse@mandriva.org> 0.4.8-5
+ Revision: 655808
- rebuild for fixed redland (LV2 support was disabled)

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 0.4.8-4
+ Revision: 643882
- rebuild to obsolete old packages

* Sun Feb 13 2011 Frank Kober <emuse@mandriva.org> 0.4.8-3
+ Revision: 637436
- tighten requires

* Wed Feb 09 2011 Frank Kober <emuse@mandriva.org> 0.4.8-2
+ Revision: 637057
- rebuild for new raptor

* Thu Jan 20 2011 Frank Kober <emuse@mandriva.org> 0.4.8-1
+ Revision: 631906
- new version 0.4.8

* Sun Oct 17 2010 Frank Kober <emuse@mandriva.org> 0.4.7-1mdv2011.0
+ Revision: 586281
- new version 0.4.7

* Sat May 22 2010 Frank Kober <emuse@mandriva.org> 0.4.6-1mdv2011.0
+ Revision: 545709
- new version 0.4.6 (numerous bugfixes, some new features)
- adjust icon file path
- add DESTDIR to makeinstall step

* Mon May 03 2010 Frank Kober <emuse@mandriva.org> 0.4.5-3mdv2010.1
+ Revision: 541876
- fix desktop categories, use silent setup

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - slv2-devel already requires lv2core-devel

* Thu Apr 22 2010 Frank Kober <emuse@mandriva.org> 0.4.5-2mdv2010.1
+ Revision: 538023
- enable LV2 plugin support

* Sat Jan 23 2010 Frederik Himpe <fhimpe@mandriva.org> 0.4.5-1mdv2010.1
+ Revision: 495307
- update to new version 0.4.5

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 0.4.4-1mdv2010.1
+ Revision: 493271
- update to new version 0.4.4

* Wed Dec 23 2009 Frank Kober <emuse@mandriva.org> 0.4.3-2mdv2010.1
+ Revision: 481875
- bump release

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 462596
- update to new version 0.4.3

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 0.4.2-2mdv2010.0
+ Revision: 411056
- rebuild for new liblo

* Fri Jun 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 383124
- update to new version 0.4.2

* Tue May 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 372250
- update to new version 0.4.1

* Fri Mar 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.0-1mdv2009.1
+ Revision: 359036
- update to new version 0.4.0

* Mon Feb 23 2009 trem <trem@mandriva.org> 0.3.0-1mdv2009.1
+ Revision: 344292
- update to 0.3.0

* Sat Dec 06 2008 trem <trem@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 311232
- import qtractor



Summary:	A tetris clone for Linux
Summary(pl):	Klon tetrisa dla Linuxa
Name:		ltris
Version:	1.0.3
Release:	1
License:	GPL
Vendor:		Michael Speck <kulkanie@gmx.net>
Group:		X11/Applications/Games
Source0:	http://ftp1.sourceforge.net/lgames/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Icon:		ltris16.xpm
URL:		http://www.lgames.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_xbindir	%{_prefix}/bin
%define		_ltrisdata	%{_datadir}/LTris
%description
LTris is a clone of the tetris game for Linux. It uses a SDL library.

%description -l pl
LTris jest klonem gry tetris dla Linuxa. Korzysta on z biblioteki SDL.

%prep
%setup -qn %{name}-%{version}

%build
OPTFLAGS="%{rpmcflags}" CC="%{__cc}"
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xbindir},%{_pixmapsdir},%{_applnkdir}/Games,%{_ltrisdata}/sounds,%{_ltrisdata}/icons,%{_ltrisdata}/gfx}

install src/ltris $RPM_BUILD_ROOT%{_xbindir}/ltris
install icons/ltris16.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/ltris16.xpm
install src/sounds/*wav $RPM_BUILD_ROOT%{_ltrisdata}/sounds
install src/gfx/*bmp $RPM_BUILD_ROOT%{_ltrisdata}/gfx
install icons/*xpm	$RPM_BUILD_ROOT%{_ltrisdata}/icons
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_xbindir}/*
%{_applnkdir}/Games/ltris.desktop
%{_pixmapsdir}/*.xpm
%{_datadir}/LTris

Summary:	A tetris clone for Linux
Summary(pl):	Klon tetrisa dla Linuksa
Name:		ltris
Version:	1.0.3
Release:	4
License:	GPL v2+
Vendor:		Michael Speck <kulkanie@gmx.net>
Group:		X11/Applications/Games
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/lgames/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Icon:		ltris16.xpm
URL:		http://www.lgames.org/
BuildRequires:	SDL >= 1.2.4 
BuildRequires:	SDL_mixer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_ltrisdata	%{_datadir}/games/ltris

%description
LTris is a clone of the tetris game for Linux. It uses a SDL library.

%description -l pl
LTris jest klonem gry tetris dla Linuksa. Korzysta z biblioteki SDL.

%prep
%setup -q

%build
%configure2_13 \
	--with-highscore-path=/var/games

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_ltrisdata}/{sounds,icons,gfx}} \
	$RPM_BUILD_ROOT{/var/games,%{_pixmapsdir},%{_applnkdir}/Games}

install src/ltris $RPM_BUILD_ROOT%{_bindir}
install icons/ltris16.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/ltris16.xpm
install src/sounds/*wav $RPM_BUILD_ROOT%{_ltrisdata}/sounds
install src/gfx/*bmp $RPM_BUILD_ROOT%{_ltrisdata}/gfx
install icons/*xpm	$RPM_BUILD_ROOT%{_ltrisdata}/icons
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install src/empty.hscr $RPM_BUILD_ROOT/var/games/ltris.hscr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(2755,root,games) %{_bindir}/*
%{_applnkdir}/Games/ltris.desktop
%{_pixmapsdir}/*.xpm
%{_datadir}/games/ltris
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/ltris.hscr

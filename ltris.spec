Summary:	A tetris clone for Linux
Summary(pl):	Klon tetrisa dla Linuksa
Name:		ltris
Version:	1.0.4
Release:	1
License:	GPL v2+
Vendor:		Michael Speck <kulkanie@gmx.net>
Group:		X11/Applications/Games
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/lgames/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.lgames.org/
BuildRequires:	SDL >= 1.2.4 
BuildRequires:	SDL_mixer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games/Arcade}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(2755,root,games) %{_bindir}/*
%{_applnkdir}/Games/Arcade/ltris.desktop
%{_pixmapsdir}/*
%{_datadir}/games/ltris
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/ltris.hscr

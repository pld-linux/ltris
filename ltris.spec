Summary:	A tetris clone for Linux
Summary(pl):	Klon tetrisa dla Linuksa
Name:		ltris
Version:	1.0.7
Release:	1
License:	GPL v2+
Vendor:		Michael Speck <kulkanie@gmx.net>
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	2c80799136607429b8cb7d50093ca56c
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://lgames.sourceforge.net/index.php?project=LTris
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/games

%description
LTris is a clone of the tetris game for Linux. It uses a SDL library.

%description -l pl
LTris jest klonem gry tetris dla Linuksa. Korzysta z biblioteki SDL.

%prep
%setup -q

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(2755,root,games) %{_bindir}/*
%{_desktopdir}/ltris.desktop
%{_pixmapsdir}/*.png
%{_datadir}/ltris
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/ltris.hscr

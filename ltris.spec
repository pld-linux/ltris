Summary:	A tetris clone for Linux
Summary(pl.UTF-8):	Klon tetrisa dla Linuksa
Name:		ltris
Version:	1.0.19
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	63486b90e59699823f7093bc9ab87725
Patch0:		%{name}-desktop.patch
URL:		http://lgames.sourceforge.net/LTris
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_mixer-devel
BuildRequires:	gettext-tools
Requires:	SDL >= 1.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/games

%description
LTris is a clone of the Tetris game for Linux. It uses a SDL library.

%description -l pl.UTF-8
LTris jest klonem gry Tetris dla Linuksa. Korzysta z biblioteki SDL.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(2755,root,games) %{_bindir}/ltris
%{_desktopdir}/ltris.desktop
%{_pixmapsdir}/ltris48.gif
%{_datadir}/ltris
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/ltris.hscr

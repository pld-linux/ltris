Summary:	A tetris clone for Linux
Summary(pl.UTF-8):	Klon tetrisa dla Linuksa
Name:		ltris
Version:	1.3.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	c0ea65634a111f3952609e4db9b0eef4
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-format.patch
URL:		https://lgames.sourceforge.net/LTris
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	gettext-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	SDL >= 1.2.4
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/games

%description
LTris is a clone of the Tetris game for Linux. It uses a SDL library.

%description -l pl.UTF-8
LTris jest klonem gry Tetris dla Linuksa. Korzysta z biblioteki SDL.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
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

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(2755,root,games) %{_bindir}/ltris
%{_desktopdir}/ltris.desktop
%{_iconsdir}/hicolor/48x48/apps/ltris.png
%{_datadir}/ltris
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/ltris.hscr

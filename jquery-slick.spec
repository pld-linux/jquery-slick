%define		plugin	slick
Summary:	the last carousel you'll ever need
Name:		jquery-%{plugin}
Version:	1.5.8
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/kenwheeler/slick/archive/%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	c8a86463f29b807ed58b93564c4878c6
URL:		http://kenwheeler.github.io/slick/
BuildRequires:	unzip
Requires:	jquery >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Carousel plugin. Fully responsive. Scales with its container.

- Separate settings per breakpoint
- Uses CSS3 when available. Fully functional when not.
- Swipe enabled. Or disabled, if you prefer.
- Desktop mouse dragging
- Infinite looping.
- Fully accessible with arrow key navigation
- Add, remove, filter & unfilter slides
- Autoplay, dots, arrows, callbacks, etc...

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qn %{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p slick/%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

cp -p slick/%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

cp -p slick/%{plugin}.css $RPM_BUILD_ROOT%{_appdir}
cp -p slick/%{plugin}-theme.css $RPM_BUILD_ROOT%{_appdir}
cp -a slick/fonts $RPM_BUILD_ROOT%{_appdir}
cp -a slick/*.gif $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown CONTRIBUTING.markdown LICENSE
%{_appdir}

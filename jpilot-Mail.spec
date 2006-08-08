#
# TODO:
# - fix auto* and send fixes to author,
# - cleanups at %install stage
#
# Attention! Doesn't work with jpilot compiled with gtk2,
#
Summary:	A mail-plugin for jpilot
Summary(pl):	Wtyczka obs³uguj±ca pocztê dla jpilota
Name:		jpilot-Mail
Version:	0.0.6
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.innominate.org/oku/jpilot-Mail/%{name}-%{version}.tar.gz
# Source0-md5:	92be56068d051d3a0e12ffdbf0d06521
Patch0:		%{name}-header.patch
URL:		http://www.innominate.org/~oku/jpilot-Mail/
BuildRequires:	gtk+-devel
BuildRequires:	pilot-link-devel
Requires:	jpilot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_jpluginsdir	/usr/lib/jpilot/plugins

%description
jpilot-Mail is a plugin for jpilot which enables you to deliver
mail that was written on your pilot and upload mail that you
received to your pilot.

%description -l pl
jpilot-Mail jest wtyczk± do jpilota która pozwala na dostarczanie
poczty napisanej na palmie oraz przes³anie odebranej poczty do palma.

%prep
%setup -q
%patch0 -p1

%build
# dont call any auto scripts - it's completly broken
%configure2_13
%{__make} \
	CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_jpluginsdir}
mv -f $RPM_BUILD_ROOT/usr/lib/lib* $RPM_BUILD_ROOT%{_jpluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%{_jpluginsdir}/*

#
# TODO:
# - fix auto* and send fixes to author,
# - cleanups at %install stage
# - pl desc + summary
#
# Attention! Doesn't work with jpilot compiled with gtk1,
#
Summary:	A mail-plugin for jpilot
Name:		jpilot-Mail
Version:	0.0.6
Release:	0.1
Group:		Applications/Communications
Source0:	ftp://ftp.innominate.org/oku/jpilot-Mail/%{name}-%{version}.tar.gz
# Source0-md5:	92be56068d051d3a0e12ffdbf0d06521
Patch0:		%{name}-header.patch
URL:		http://www.innominate.org/~oku/jpilot-Mail/
License:	GPL
Requires:       jpilot
BuildRequires:	pilot-link-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		_jpluginsdir	/usr/lib/jpilot/plugins

%description
jpilot-Mail is a plugin for jpilot (http://jpilot.linuxbox.com) which
enables you to deliver mail that was written on your pilot and upload
mail that you received to your pilot. Author: Oliver Kurth
<oliver.kurth@innominate.de>

%prep
%setup -q
%patch -p1

%build
# dont call any auto scripts - it's completly broken
%configure2_13
%{__make} CC="gcc %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_jpluginsdir}
mv $RPM_BUILD_ROOT/usr/lib/lib* $RPM_BUILD_ROOT/%{_jpluginsdir}

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS COPYING INSTALL README TODO AUTHORS
%{_jpluginsdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

Summary:	A mail-plugin for jpilot
Name:		jpilot-Mail
Version:	0.0.6
Release:	0.1
Group:		Applications/Communications
Source0:	ftp://ftp.innominate.org/oku/jpilot-Mail/%{name}-%{version}.tar.gz
URL:		http://www.innominate.org/~oku/jpilot-Mail/
Requires:       jpilot
BuildRequires:	pilot-link-devel
BuildRequires:	gtk+
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jpilot-Mail is a plugin for jpilot (http://jpilot.linuxbox.com) which
enables you to deliver mail that was written on your pilot and upload
mail that you received to your pilot. Author: Oliver Kurth
<oliver.kurth@innominate.de>

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-pl-test
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS COPYING INSTALL README TODO AUTHORS
%defattr(-,root,root)
%{_libdir}/jpilot/plugins/*

%clean
rm -rf $RPM_BUILD_ROOT

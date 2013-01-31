Name:       tel-plugin-imcmodem
Summary:    telephony plugin library for AT communication with IMC modem
Version:    0.1.4
Release:    1
Group:      System/Libraries
License:    Apache
Source0:    tel-plugin-imcmodem-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(tcore)

%description
imcmodem plugin for telephony

%prep
%setup -q

%build
%cmake .
make %{?jobs:-j%jobs}

%post
/sbin/ldconfig

%postun -p /sbin/ldconfig

%install
%make_install
mkdir -p %{buildroot}/usr/share/license

%files
%manifest tel-plugin-imcmodem.manifest
%defattr(-,root,root,-)
%{_libdir}/telephony/plugins/*
/usr/share/license/tel-plugin-imcmodem

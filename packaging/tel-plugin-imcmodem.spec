Name:       tel-plugin-imcmodem
Summary:    telephony plugin library for AT communication with IMC modem
Version:    0.1.10
Release:    1
Group:      System/Libraries
License:    Apache-2.0
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
cp LICENSE %{buildroot}/usr/share/license/%{name}

%files
%manifest tel-plugin-imcmodem.manifest
%defattr(-,root,root,-)
%{_libdir}/telephony/plugins/*
/usr/share/license/%{name}

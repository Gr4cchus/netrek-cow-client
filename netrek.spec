%global commit0 815d9a41a6b22f613dcbe2f5582fd6e2fe8e61da
%global gittag0 refs/heads/master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


Name:           netrek-client-cow
Version:        3.3.1
Release:        1%{?dist}
Summary:        COW Netrek client

License:        MIT
URL:            http://www.netrek.org/
Source0:        https://github.com/quozl/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: libtool
BuildRequires: SDL  
BuildRequires: SDL-devel  
BuildRequires: SDL_mixer  
BuildRequires: SDL_mixer-devel 
BuildRequires: autoconf 
BuildRequires: automake  
BuildRequires: bash 
BuildRequires: binutils  
BuildRequires: coreutils 
BuildRequires: cpio  
BuildRequires: diffutils 
BuildRequires: dwz 
BuildRequires: elfutils 
BuildRequires: file 
BuildRequires: findutils 
BuildRequires: gawk 
BuildRequires: gcc 
BuildRequires: glibc 
BuildRequires: glibc-common 
BuildRequires: glibc-devel 
BuildRequires: glibc-headers 
#BuildRequires: glibc-headers 
BuildRequires: grep  
BuildRequires: gzip
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: hostname
%endif # 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: imlib2  
BuildRequires: imlib2-devel 
#BuildRequires: imlib2-devel  
BuildRequires: kernel-headers 
BuildRequires: libX11 
BuildRequires: libX11-devel  
#BuildRequires: libX11-devel 
BuildRequires: libXpm 
BuildRequires: libXpm-devel 
BuildRequires: libXt-devel 
#BuildRequires: libXt-devel 
BuildRequires: libXxf86vm        


%description
Netrek is a multi-player battle simulation with a Star Trek theme. As a player, you captain starships to engage enemy vessels, bomb armies and invade planets in order to expand your team's space empire. The ultimate goal is to genocide the enemy race, but the carnage of battles along the way is ruthlessly fast paced and a lot of fun! 


%prep
%autosetup -n %{name}-%{commit0}



%build
%{_topdir}/BUILD/%{name}-%{commit0}/autogen.sh
%configure
%make_build


%install
#rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p %{buildroot}/%{_bindir}/
mv %{buildroot}/usr/games/%{name} %{buildroot}/%{_bindir}


%files
%license COPYING
%doc CHANGES README.* TODO *.DOC COPYING XTREKRC.example copyright*.h
%doc cow.html index.orig.html newbie.html cow.css stars.gif netrekrc.example
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}/*
%{_datadir}/applications/%{name}.desktop


%changelog
* Sun Feb  5 2017 Alex
- 

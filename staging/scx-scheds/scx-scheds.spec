Name:           scx-scheds
# renovate: datasource=github-releases depName=sched-ext/scx
Version:        1.0.11
Release:        1%{?dist}
Summary:        Sched_ext Schedulers and Tools

License:        GPL=2.0
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  meson >= 1.2
BuildRequires:  python
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang >= 17
BuildRequires:  llvm >= 17
BuildRequires:  lld >= 17
BuildRequires:  elfutils-libelf
BuildRequires:  elfutils-libelf-devel
BuildRequires:  zlib
BuildRequires:  jq
BuildRequires:  jq-devel
BuildRequires:  systemd
Requires:  elfutils-libelf
Requires:  zlib
Requires:  jq

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This repository contains various scheduler implementations and support utilities.

%prep
%autosetup -n scx-%{version}

%build
%meson \
 -Dsystemd=enabled \
 -Dopenrc=disabled \
 -Dlibalpm=disabled
%meson_build

%install
%meson_install

%files
%{_bindir}/*
%{_prefix}/lib/systemd/system/scx_loader.service
%{_prefix}/lib/systemd/system/scx.service
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/default/scx
%{_datadir}/dbus-1/system.d/org.scx.Loader.conf
%{_datadir}/dbus-1/system-services/org.scx.Loader.service

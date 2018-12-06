# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/reactions
%global commit          f2e0b4ca5b8268a0c20f3ec187f0c739266547d8

%global common_description %{expand:
Reactions service definition for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Reactions service definition for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/shurcooL/htmlg)
BuildRequires: golang(github.com/shurcooL/octicon)
BuildRequires: golang(github.com/shurcooL/users)
BuildRequires: golang(github.com/shurcooL/webdavfs/vfsutil)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)
BuildRequires: golang(golang.org/x/net/webdav)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181026gitf2e0b4c
- Bump to commit f2e0b4ca5b8268a0c20f3ec187f0c739266547d8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitb971588
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420gitb971588
- First package for Fedora


Summary:	Emacs support for LaTeX cross-references, citations
Summary(pl):	Wsparcie dla LaTeXowych referencji i cytat�w
Name:		xemacs-reftex-pkg
%define		srcname	reftex
Version:	1.33
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	4d9a603199ad55c5d3f3cd31413a56de
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildRequires:	texinfo
Requires:	xemacs
Requires:	xemacs-base-pkg
Requires:	xemacs-fsf-compat-pkg
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Emacs support for LaTeX cross-references, citations.

%description -l pl
Wsparcie dla LaTeXowych referencji i cytat�w.

%prep
%setup -q -c
%patch0 -p1

%build
(cd man/reftex; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages/lisp,%{_infodir}}

cp -a lisp/* $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp
install info/*.info* $RPM_BUILD_ROOT%{_infodir}

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/reftex/ChangeLog etc/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_infodir}/*.info*

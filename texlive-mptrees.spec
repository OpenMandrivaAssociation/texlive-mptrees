Name:		texlive-mptrees
Version:	66952
Release:	1
Summary:	Probability trees with MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mptrees
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mptrees.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mptrees.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides MetaPost tools for drawing simple
probability trees. One command and several parameters to
control the output are provided.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/metapost/mptrees
%doc %{_texmfdistdir}/doc/metapost/mptrees

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

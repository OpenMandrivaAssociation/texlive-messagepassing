Name:		texlive-messagepassing
Version:	63116
Release:	2
Summary:	Draw diagrams to represent communication protocols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/messagepassing
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/messagepassing.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/messagepassing.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/messagepassing.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an environment to easily draw diagrams to
represent communication protocols using message passing among
processes. Processes are represented as horizontal or vertical
lines, and communications as arrows between lines. The package
also provides multiple macros to decorate those diagrams, for
instance to annotate the diagram, to add crashes to the
processes, checkpoints, ...

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/messagepassing
%{_texmfdistdir}/tex/latex/messagepassing
%doc %{_texmfdistdir}/doc/latex/messagepassing

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

%global tl_name messagepassing
%global tl_revision 69123

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Draw diagrams to represent communication protocols
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/messagepassing
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/messagepassing.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/messagepassing.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/messagepassing.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an environment to easily draw diagrams to
represent communication protocols using message passing among processes.
Processes are represented as horizontal or vertical lines, and
communications as arrows between lines. The package also provides
multiple macros to decorate those diagrams, for instance to annotate the
diagram, to add crashes to the processes, checkpoints, ...


%global tl_name engpron
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2
Release:	%{tl_revision}.1
Summary:	Helps to type the pronunciation of English words
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/engpron
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros beginning with the PS character, made
active, which enable us to write the British or American English
pronunciation as one can find it in the 'English Pronouncing Dictionary'
by Daniel Jones. There is an option to typeset the pronunciation in the
style of Harrap's dictionary.


Name:		texlive-engpron
Version:	2
Release:	1
Summary:	Helps to type the pronunciation of English words
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/engpron
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides macros beginning with the '' character,
made active, which enable us to write the British or American
English pronunciation as one can find it in the 'English
Pronouncing Dictionary' by Daniel Jones. There is an option to
typeset the pronunciation in the style of Harrap's dictionary.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/engpron/engpron-tools.sty
%{_texmfdistdir}/tex/latex/engpron/engpron.sty
%doc %{_texmfdistdir}/doc/latex/engpron/LISEZMOI
%doc %{_texmfdistdir}/doc/latex/engpron/README
%doc %{_texmfdistdir}/doc/latex/engpron/engpron-en.ltx
%doc %{_texmfdistdir}/doc/latex/engpron/engpron-en.pdf
%doc %{_texmfdistdir}/doc/latex/engpron/engpron-ex-en.pdf
%doc %{_texmfdistdir}/doc/latex/engpron/engpron-ex-en.tex
%doc %{_texmfdistdir}/doc/latex/engpron/engpron-ex-fr.pdf
%doc %{_texmfdistdir}/doc/latex/engpron/engpron-ex-fr.tex
%doc %{_texmfdistdir}/doc/latex/engpron/engpron-fr.ltx
%doc %{_texmfdistdir}/doc/latex/engpron/engpron-fr.pdf
%doc %{_texmfdistdir}/doc/latex/engpron/engpron.pdf
#- source
%doc %{_texmfdistdir}/source/latex/engpron/Makefile
%doc %{_texmfdistdir}/source/latex/engpron/engpron.dtx
%doc %{_texmfdistdir}/source/latex/engpron/engpron.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
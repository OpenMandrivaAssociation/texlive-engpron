Name:		texlive-engpron
Version:	16558
Release:	1
Summary:	Helps to type the pronunciation of English words
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/engpron
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engpron.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros beginning with the '' character,
made active, which enable us to write the British or American
English pronunciation as one can find it in the 'English
Pronouncing Dictionary' by Daniel Jones. There is an option to
typeset the pronunciation in the style of Harrap's dictionary.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

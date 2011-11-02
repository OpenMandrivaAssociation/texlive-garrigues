Name:		texlive-garrigues
Version:	20091110
Release:	1
Summary:	MetaPost macros for the reproduction of Garrigues' Easter nomogram
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/garrigues
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garrigues.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garrigues.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Metapost macros for the reproduction of Garrigues' Easter
nomogram. These macros are described in Denis Roegel: An
introduction to nomography: Garrigues' nomogram for the
computation of Easter, TUGboat (volume 30, number 1, 2009,
pages 88-104).

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
%{_texmfdistdir}/metapost/garrigues/garrigues.mp
%doc %{_texmfdistdir}/doc/metapost/garrigues/README
%doc %{_texmfdistdir}/doc/metapost/garrigues/article.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
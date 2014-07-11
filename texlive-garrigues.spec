# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/garrigues
# catalog-date 2009-11-10 09:15:37 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-garrigues
Version:	20091110
Release:	8
Summary:	MetaPost macros for the reproduction of Garrigues' Easter nomogram
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/garrigues
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garrigues.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garrigues.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Metapost macros for the reproduction of Garrigues' Easter
nomogram. These macros are described in Denis Roegel: An
introduction to nomography: Garrigues' nomogram for the
computation of Easter, TUGboat (volume 30, number 1, 2009,
pages 88-104).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091110-2
+ Revision: 752182
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091110-1
+ Revision: 718519
- texlive-garrigues
- texlive-garrigues
- texlive-garrigues
- texlive-garrigues


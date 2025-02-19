Name:		texlive-garrigues
Version:	15878
Release:	2
Summary:	MetaPost macros for the reproduction of Garrigues' Easter nomogram
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/garrigues
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garrigues.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garrigues.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}

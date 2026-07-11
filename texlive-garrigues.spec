%global tl_name garrigues
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	MetaPost macros for the reproduction of Garrigues Easter nomogram
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/garrigues
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/garrigues.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/garrigues.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
MetaPost macros for the reproduction of Garrigues' Easter nomogram.
These macros are described in Denis Roegel: An introduction to
nomography: Garrigues' nomogram for the computation of Easter, TUGboat
(volume 30, number 1, 2009, pages 88-104)


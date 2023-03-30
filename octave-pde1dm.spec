%global octpkg pde1dm

Summary:	1D Partial Differential Equation Solver for MATLAB and Octave
Name:		octave-pde1dm
Version:	1.3
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/pde1dm/
Url:		https://github.com/wgreene310/pde1dm/
Source0:	https://github.com/wgreene310/pde1dm/archive/v%{version}/pde1dm-%{version}.tar.gz

BuildRequires:  octave-devel >= 7.1.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Solve systems of partial differential equations (PDE) in a single 
spatial variable and time. The input is mostly compatible with the 
MATLAB function pdepe. Many pdepe examples will work with pde1dm with 
only small changes.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}
# remove non utf-8 chars
sed -i -e "s/[\x80-\xFF]//g" multiprod.m

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild


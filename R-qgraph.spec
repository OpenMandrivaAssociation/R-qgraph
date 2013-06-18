%global packname  qgraph
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.1
Release:          2
Summary:          Network representations of relationships in data
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-psych R-ellipse R-lavaan R-sem R-plyr 
Requires:         R-RSVGTipsDevice R-tikzDevice R-fdrtool R-lavaan R-sem 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-psych R-ellipse R-lavaan R-sem R-plyr 
BuildRequires:    R-RSVGTipsDevice R-tikzDevice R-fdrtool R-lavaan R-sem 

%description
The qgraph package can be used to visualize data as networks.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

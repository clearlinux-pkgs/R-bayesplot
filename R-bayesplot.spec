#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bayesplot
Version  : 1.5.0
Release  : 5
URL      : https://cran.r-project.org/src/contrib/bayesplot_1.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bayesplot_1.5.0.tar.gz
Summary  : Plotting for Bayesian Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-dplyr
Requires: R-ggridges
Requires: R-rlang
BuildRequires : R-dplyr
BuildRequires : R-ggridges
BuildRequires : R-rlang
BuildRequires : clr-R-helpers

%description
and MCMC diagnostics. The package is designed not only to provide convenient
    functionality for users, but also a common set of functions that can be
    easily used by developers working on a variety of R packages for Bayesian
    modeling, particularly (but not exclusively) packages interfacing with 'Stan'.

%prep
%setup -q -c -n bayesplot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522436891

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522436891
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bayesplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bayesplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bayesplot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bayesplot|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bayesplot/DESCRIPTION
/usr/lib64/R/library/bayesplot/INDEX
/usr/lib64/R/library/bayesplot/Meta/Rd.rds
/usr/lib64/R/library/bayesplot/Meta/features.rds
/usr/lib64/R/library/bayesplot/Meta/hsearch.rds
/usr/lib64/R/library/bayesplot/Meta/links.rds
/usr/lib64/R/library/bayesplot/Meta/nsInfo.rds
/usr/lib64/R/library/bayesplot/Meta/package.rds
/usr/lib64/R/library/bayesplot/Meta/vignette.rds
/usr/lib64/R/library/bayesplot/NAMESPACE
/usr/lib64/R/library/bayesplot/NEWS.md
/usr/lib64/R/library/bayesplot/R/bayesplot
/usr/lib64/R/library/bayesplot/R/bayesplot.rdb
/usr/lib64/R/library/bayesplot/R/bayesplot.rdx
/usr/lib64/R/library/bayesplot/R/sysdata.rdb
/usr/lib64/R/library/bayesplot/R/sysdata.rdx
/usr/lib64/R/library/bayesplot/doc/graphical-ppcs.R
/usr/lib64/R/library/bayesplot/doc/graphical-ppcs.Rmd
/usr/lib64/R/library/bayesplot/doc/graphical-ppcs.html
/usr/lib64/R/library/bayesplot/doc/index.html
/usr/lib64/R/library/bayesplot/doc/plotting-mcmc-draws.R
/usr/lib64/R/library/bayesplot/doc/plotting-mcmc-draws.Rmd
/usr/lib64/R/library/bayesplot/doc/plotting-mcmc-draws.html
/usr/lib64/R/library/bayesplot/doc/visual-mcmc-diagnostics.R
/usr/lib64/R/library/bayesplot/doc/visual-mcmc-diagnostics.Rmd
/usr/lib64/R/library/bayesplot/doc/visual-mcmc-diagnostics.html
/usr/lib64/R/library/bayesplot/help/AnIndex
/usr/lib64/R/library/bayesplot/help/aliases.rds
/usr/lib64/R/library/bayesplot/help/bayesplot.rdb
/usr/lib64/R/library/bayesplot/help/bayesplot.rdx
/usr/lib64/R/library/bayesplot/help/figures/bayesplot1.png
/usr/lib64/R/library/bayesplot/help/figures/bayesplot2.png
/usr/lib64/R/library/bayesplot/help/figures/bayesplot3.png
/usr/lib64/R/library/bayesplot/help/figures/stanlogo.png
/usr/lib64/R/library/bayesplot/help/paths.rds
/usr/lib64/R/library/bayesplot/html/00Index.html
/usr/lib64/R/library/bayesplot/html/R.css

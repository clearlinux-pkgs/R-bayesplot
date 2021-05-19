#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bayesplot
Version  : 1.8.0
Release  : 44
URL      : https://cran.r-project.org/src/contrib/bayesplot_1.8.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bayesplot_1.8.0.tar.gz
Summary  : Plotting for Bayesian Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-dplyr
Requires: R-ggplot2
Requires: R-ggridges
Requires: R-glue
Requires: R-reshape2
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyselect
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-ggridges
BuildRequires : R-glue
BuildRequires : R-reshape2
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : buildreq-R

%description
prior and posterior predictive checks, and other visualizations 
    to support the applied Bayesian workflow advocated in

%prep
%setup -q -c -n bayesplot
cd %{_builddir}/bayesplot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610301991

%install
export SOURCE_DATE_EPOCH=1610301991
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc bayesplot || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bayesplot/CITATION
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
/usr/lib64/R/library/bayesplot/tests/testthat.R
/usr/lib64/R/library/bayesplot/tests/testthat/data-for-binomial.rda
/usr/lib64/R/library/bayesplot/tests/testthat/data-for-mcmc-tests.R
/usr/lib64/R/library/bayesplot/tests/testthat/data-for-ppc-tests.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-aesthetics.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-available_ppc.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-bayesplot_grid.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-convenience-functions.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-example-draws.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-extractors.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-helpers-mcmc.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-helpers-ppc.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-helpers-shared.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-mcmc-combo.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-mcmc-diagnostics.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-mcmc-distributions.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-mcmc-intervals.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-mcmc-nuts.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-mcmc-recover.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-mcmc-scatter-and-parcoord.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-mcmc-traces.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-pp_check.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-discrete.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-distributions.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-errors.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-input-validation.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-intervals.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-loo.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-scatterplots.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-test-statistics.R

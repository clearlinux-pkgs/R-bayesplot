#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v24
# autospec commit: a88ffdc
#
Name     : R-bayesplot
Version  : 1.12.0
Release  : 70
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/bayesplot_1.12.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/bayesplot_1.12.0.tar.gz
Summary  : Plotting for Bayesian Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-dplyr
Requires: R-ggplot2
Requires: R-ggridges
Requires: R-glue
Requires: R-posterior
Requires: R-reshape2
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyr
Requires: R-tidyselect
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-ggridges
BuildRequires : R-glue
BuildRequires : R-posterior
BuildRequires : R-reshape2
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
prior and posterior predictive checks, and other visualizations
    to support the applied Bayesian workflow advocated in

%prep
%setup -q -n bayesplot
pushd ..
cp -a bayesplot buildavx2
popd
pushd ..
cp -a bayesplot buildavx512
popd
pushd ..
cp -a bayesplot buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744319323

%install
export SOURCE_DATE_EPOCH=1744319323
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mapxf -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mapxf -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/bayesplot/help/figures/logo.svg
/usr/lib64/R/library/bayesplot/help/figures/stanlogo.png
/usr/lib64/R/library/bayesplot/help/paths.rds
/usr/lib64/R/library/bayesplot/html/00Index.html
/usr/lib64/R/library/bayesplot/html/R.css
/usr/lib64/R/library/bayesplot/tests/testthat.R
/usr/lib64/R/library/bayesplot/tests/testthat/data-for-binomial.rda
/usr/lib64/R/library/bayesplot/tests/testthat/data-for-mcmc-tests.R
/usr/lib64/R/library/bayesplot/tests/testthat/data-for-ordinal.rda
/usr/lib64/R/library/bayesplot/tests/testthat/data-for-ppc-tests.R
/usr/lib64/R/library/bayesplot/tests/testthat/helper.R
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
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-censoring.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-discrete.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-distributions.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-errors.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-input-validation.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-intervals.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-loo.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-scatterplots.R
/usr/lib64/R/library/bayesplot/tests/testthat/test-ppc-test-statistics.R

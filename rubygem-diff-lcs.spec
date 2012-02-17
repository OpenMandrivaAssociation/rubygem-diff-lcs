# Generated from diff-lcs-1.1.2.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	diff-lcs

Summary:	Provides a list of changes that represent the difference between two sequenced collections
Name:		rubygem-%{rbname}

Version:	1.1.2
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://rubyforge.org/projects/ruwiki/
Source0:	%{rbname}-%{version}.gem
Patch0:		diff-lcs-1.1.2-add-missing-tag-to-metadata.patch
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest
common subsequence (LCS) algorithm to compute intelligent differences between
two sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
gunzip metadata.gz
%patch0 -p1 -b .tag~
gzip metadata

%build
%gem_build -f tests

%install
%gem_install

%files
%{_bindir}/htmldiff
%{_bindir}/ldiff
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/htmldiff
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/ldiff
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/diff
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/diff/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/diff/lcs
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/diff/lcs/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/ChangeLog
%{ruby_gemdir}/gems/%{rbname}-%{version}/Install
%{ruby_gemdir}/gems/%{rbname}-%{version}/README
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*.rb

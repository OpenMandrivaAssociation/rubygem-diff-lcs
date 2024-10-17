%define oname   diff-lcs

Name:       rubygem-%{oname}
Version:    1.1.3
Release:    4
Summary:    Provides a list of changes
Group:      Development/Ruby
License:    GPLv2+
URL:        https://rubyforge.org/projects/ruwiki/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRequires: rubygems
BuildRequires: rubygem(rake)
BuildRequires: rubygem(archive-tar-minitar)
BuildArch:  noarch

%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest
common subsequence (LCS) algorithm to compute intelligent differences
between two sequenced enumerable containers. The implementation is based on
Mario I. Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).

#-------------------------------------------------------------------------------
%package        doc
Summary:    Documentation for %{name}
Group:      Development/Ruby
Requires:   %{name} = %{version}-%{release}

%description    doc
Documents, Rdoc & RI documentation for %{name}.
#-------------------------------------------------------------------------------

%prep
%setup -q
tar xmf data.tar.gz

%build
%gem_build

%install
%gem_install
rm -rf %{buildroot}%{gem_dir}/gems/%{oname}-%{version}/.yardoc

# Fix Wrong interpreter
sed -i '/^#!/d' %{buildroot}%{gem_dir}/gems/%{oname}-%{version}/lib/diff/{lcs/*.rb,lcs.rb}

%files
%{_bindir}/ldiff
%{_bindir}/htmldiff
%dir %{gem_dir}/gems/%{oname}-%{version}/
%{gem_dir}/gems/%{oname}-%{version}/bin
%{gem_dir}/gems/%{oname}-%{version}/lib
%{gem_dir}/specifications/%{oname}-%{version}.gemspec

%files          doc
%doc %{gem_dir}/doc/%{oname}-%{version}
%doc %{gem_dir}/gems/%{oname}-%{version}/docs/COPYING.txt
%doc %{gem_dir}/gems/%{oname}-%{version}/README.rdoc
%doc %{gem_dir}/gems/%{oname}-%{version}/History.rdoc
%doc %{gem_dir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{gem_dir}/gems/%{oname}-%{version}/License.rdoc

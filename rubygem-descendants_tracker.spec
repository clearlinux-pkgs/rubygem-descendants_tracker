#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-descendants_tracker
Version  : 0.0.4
Release  : 4
URL      : https://rubygems.org/downloads/descendants_tracker-0.0.4.gem
Source0  : https://rubygems.org/downloads/descendants_tracker-0.0.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# descendants_tracker
[![Gem Version](https://badge.fury.io/rb/descendants_tracker.png)][gem]
[![Build Status](https://secure.travis-ci.org/dkubb/descendants_tracker.png?branch=master)][travis]
[![Dependency Status](https://gemnasium.com/dkubb/descendants_tracker.png)][gemnasium]
[![Code Climate](https://codeclimate.com/github/dkubb/descendants_tracker.png)][codeclimate]
[![Coverage Status](https://coveralls.io/repos/dkubb/descendants_tracker/badge.png?branch=master)][coveralls]

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n descendants_tracker-0.0.4
gem spec %{SOURCE0} -l --ruby > rubygem-descendants_tracker.gemspec

%build
gem build rubygem-descendants_tracker.gemspec

%install
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
descendants_tracker-0.0.4.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/descendants_tracker-0.0.4.gem
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/DescendantsTracker/add_descendant-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/DescendantsTracker/cdesc-DescendantsTracker.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/DescendantsTracker/descendants-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/DescendantsTracker/extended-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/DescendantsTracker/inherited-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/DescendantsTracker/setup-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/page-CONTRIBUTING_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/page-LICENSE.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/descendants_tracker-0.0.4/ri/page-TODO.ri
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/.ruby-gemset
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/Gemfile.devtools
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/Guardfile
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/README.md
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/TODO
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/config/devtools.yml
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/config/flay.yml
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/config/flog.yml
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/config/mutant.yml
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/config/reek.yml
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/config/rubocop.yml
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/config/yardstick.yml
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/descendants_tracker.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/lib/descendants_tracker.rb
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/lib/descendants_tracker/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/spec/rcov.opts
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/spec/spec.opts
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/spec/support/config_alias.rb
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/spec/unit/descendants_tracker/add_descendant_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/spec/unit/descendants_tracker/descendants_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/descendants_tracker-0.0.4/spec/unit/descendants_tracker/inherited_spec.rb
/usr/lib64/ruby/gems/2.2.0/specifications/descendants_tracker-0.0.4.gemspec

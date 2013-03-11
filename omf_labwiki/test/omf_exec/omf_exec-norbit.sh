#!/bin/bash

LW_HOME=$HOME/GIMI/omf_labwiki/test/omf_exec
OMF_HOME=$HOME/omf5_4
CWD=$(dirname $0)

[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
rvm use ruby-1.8.7

#ruby -I $OMF_HOME/omf-expctl/ruby -I $OMF_HOME/omf-common/ruby $OMF_HOME/omf-expctl/ruby/omf-expctl.rb \
#  -C $CWD/etc/omf-expctl.norbit.yaml --log $CWD/etc/omf-expctl_log.xml $*

#ruby -r rubygems -I $OMF_HOME/omf-expctl/ruby -I $OMF_HOME/omf-common/ruby $OMF_HOME/omf-expctl/ruby/omf-expctl.rb \
#     -C /etc/omf-expctl-5.4/omf-expctl.yaml -S gimic30 --log $CWD/etc/omf-expctl_log.xml $*

#omf-5.4 exec --no-am -C /home/cong/work/labwiki/test/omf_exec/omf-expctl.yaml -e gimi-test-1 -S gimic31 $*

ruby -r rubygems -I $OMF_HOME/omf-expctl/ruby -I $OMF_HOME/omf-common/ruby $OMF_HOME/omf-expctl/ruby/omf-expctl.rb \
     -C $CWD/etc/omf-expctl.exogeni.yaml --log $CWD/etc/omf-expctl_log.xml $*

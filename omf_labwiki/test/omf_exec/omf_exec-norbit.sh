#!/bin/bash

LW_HOME=$HOME/GIMI/omf_labwiki/test/omf_exec
OMF_HOME=$HOME/omf5_4
CWD=$(dirname $0)

[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
rvm use ruby-1.8.7

#iget step1-ping_all.rb /home/cong/geniRenci/home/rods/

ruby -I $OMF_HOME/omf-expctl/ruby -I $OMF_HOME/omf-common/ruby $OMF_HOME/omf-expctl/ruby/omf-expctl.rb \
  -C /home/labwiki/GIMI/omf_labwiki/test/omf_exec/omf-expctl.yaml --no-am $*

#ruby -r rubygems -I $OMF_HOME/omf-expctl/ruby -I $OMF_HOME/omf-common/ruby $OMF_HOME/omf-expctl/ruby/omf-expctl.rb \
#     -C /etc/omf-expctl-5.4/omf-expctl.yaml -S gimic30 --log $CWD/etc/omf-expctl_log.xml $*

#omf-5.4 exec --no-am -C /home/cong/work/labwiki/test/omf_exec/omf-expctl.yaml -e gimi-test-1 $*

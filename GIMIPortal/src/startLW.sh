#!/bin/bash

LWPORT=$1

LABWIKI_HOME=/home/johren/GIMI/GIMIPortal/src/omf_labwiki
OMF_HOME=/home/johren/omf_web

source ~/.rvm/scripts/rvm
#nohup ruby -I $LABWIKI_HOME/lib -I $OMF_HOME/lib $LABWIKI_HOME/lib/labwiki.rb --lw-config ~/norbit.yaml --port $LWPORT start > /dev/null &
#nohup ruby $LABWIKI_HOME/bin/labwiki --lw-config ~/norbit.yaml --port $LWPORT start > /dev/null &
nohup ruby -I $LABWIKI_HOME/lib -I $OMF_HOME/lib $LABWIKI_HOME/bin/labwiki --lw-config ~/norbit.yaml --port $LWPORT start > /dev/null &

lwpid=$!

echo $lwpid > /var/run/labwiki/labwiki${LWPORT}.pid


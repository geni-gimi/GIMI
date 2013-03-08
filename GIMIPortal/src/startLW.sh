#!/bin/bash

LWPORT=$1
UNAME=$2

LABWIKI_HOME=/home/labwiki/GIMI/omf_labwiki
OMF_HOME=/home/labwiki/omf_web

source ~/.rvm/scripts/rvm
nohup ruby -I $LABWIKI_HOME/lib -I $OMF_HOME/lib $LABWIKI_HOME/bin/labwiki --lw-config /home/${UNAME}/exogeni.yaml --port $LWPORT start > /dev/null &

lwpid=$!

echo $lwpid > /var/run/labwiki/labwiki${LWPORT}.pid


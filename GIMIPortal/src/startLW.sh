#!/bin/bash

LWPORT=$1
UNAME=$2

LABWIKI_HOME=${HOME}/GIMI/omf_labwiki
OMF_HOME=${HOME}/omf_web

#source ~/.rvm/scripts/rvm
[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
ruby use ruby 1.9.3

nohup ruby -I $LABWIKI_HOME/lib -I $OMF_HOME/lib $LABWIKI_HOME/bin/labwiki --lw-config /home/${UNAME}/exogeni.yaml --port $LWPORT start > /tmp/labwiki$LWPORT.log &

lwpid=$!

echo $lwpid > /var/run/labwiki/labwiki${LWPORT}.pid


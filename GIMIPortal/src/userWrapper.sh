#!/bin/bash

ACTION=$1
LWPORT=$2
UNAME=$3
LWHOME=$4

if [ "${ACTION}" = "start" ]; then
    LABWIKI_HOME=${LWHOME}/GIMI/omf_labwiki
    OMF_HOME=${LWHOME}/omf_web
    
    [[ -s "/home/$UNAME/.rvm/scripts/rvm" ]] && . "/home/$UNAME/.rvm/scripts/rvm"
    rvm use 1.9.3 > /dev/null

    nohup ruby -I $LABWIKI_HOME/lib -I $OMF_HOME/lib $LABWIKI_HOME/bin/labwiki --lw-config /home/${UNAME}/exogeni.yaml --port $LWPORT --user $UNAME start > /tmp/labwiki$LWPORT.log &

    lwpid=$!

    echo $lwpid > /var/run/labwiki/labwiki${LWPORT}.pid
elif [ "${ACTION}" = "stop" ]; then

    lwpid=`cat /var/run/labwiki/labwiki${LWPORT}.pid`
    # verify lwpid

    ps -p ${lwpid}
    if [ $? -eq 0 ]; then
        kill $lwpid
    fi

    rm /var/run/labwiki/labwiki${LWPORT}.pid
    rm /tmp/labwiki${LWPORT}.log
fi


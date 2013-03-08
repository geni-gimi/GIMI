#!/bin/bash

LWPORT=$1

lwpid=`cat /var/run/labwiki/labwiki${LWPORT}.pid`
# verify lwpid

ps -p ${lwpid}
if [ $? -eq 0 ]; then
    kill $lwpid
fi

rm /var/run/labwiki/labwiki${LWPORT}.pid


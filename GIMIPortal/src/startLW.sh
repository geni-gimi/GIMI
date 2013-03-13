#!/bin/bash

LWPORT=$1
UNAME=$2

sudo -u $UNAME ${HOME}/GIMI/GIMIPortal/src/userWrapper.sh start $LWPORT $UNAME $HOME



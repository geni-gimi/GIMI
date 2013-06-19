#!/bin/bash

LWPORT=$1
UNAME=$2

sudo -u $UNAME ${HOME}/GIMI/GIMIPortal/src/userWrapper.sh stop $LWPORT > /tmp/checkstop 2>&1



#!/bin/bash

# Source common functions.

#. $(dirname $0)/dingbot-functions.sh

# Check if the script has already been run, and bail if it has.

#grep "Node setup done" /.gimibot-done && abend 1 "/.gimibot-done exists"

# Set a decent umask.

umask 022

# Log everything, for debugging purposes.

TIMESTAMP=$(date +"%Y%m%d.%H%M%S")
#LOGFILE=/var/log/gimibot-$TIMESTAMP.log
#exec < /dev/null > $LOGFILE 2>&1

## General things that we want on all types of nodes, pass 1

# I'm sure I'll come up with some of these.

## Node-type-specific things

# Figure out what type of node we're running on, and run the node-specific
# script for this type.
#
# For now, look for /etc/init.d/euca as a sign that we're ORCA, or
# /var/emulab as a sign that we're PG.

if [ -s /etc/init.d/neuca ]
then
  bash $(dirname $0)/postboot_script_exo.sh $*
elif [ -d /var/emulab ]
then
  bash $(dirname $0)/postboot_script.sh $*
else
  echo "$0: WARNING: Not sure what kind of node this is, setting nodetype=unknown"
fi

## General things that we want on all types of nodes, pass 2

# Put my hostname into /etc/hosts.

sed -i -re "s/^(127.0.0.1.+localhost)/\1 $(hostname)/" /etc/hosts

## Wrapup

# Create a file to indicate that we shouldn't run this script again.

#echo "Node setup done at $TIMESTAMP, log in $LOGFILE" > /.gimibot-done

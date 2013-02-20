#!/bin/bash

SLICENAME=$1
NODEID=$2
echo "hostname ${NODEID}"
hostname ${NODEID}

curl http://emmy9.casa.umass.edu/pingWrap.rb -o /root/pingWrap.rb
chmod +x /root/pingWrap.rb

curl http://emmy9.casa.umass.edu/omf-resctl.yaml -o /etc/omf-resctl-5.4/omf-resctl.yaml
perl -i.bak -pe "s/\:slice\:/\:slice\: ${SLICENAME}/g" /etc/omf-resctl-5.4/omf-resctl.yaml

/etc/init.d/omf-resctl-5.4 restart


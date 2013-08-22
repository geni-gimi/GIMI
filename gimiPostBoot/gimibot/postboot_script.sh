#!/bin/bash

cd /local/gimibot/
read -r slice</var/emulab/boot/nickname
slicename=$(echo $slice | cut -f2 -d.)

host=$(hostname)

host1=$(echo $host | cut -f1 -d.)

hostname $host1
curl http://emmy9.casa.umass.edu/pingWrap.rb -o /root/pingWrap.rb
chmod +x /root/pingWrap.rb

curl http://emmy9.casa.umass.edu/omf-resctl.yaml -o /etc/omf-resctl-5.4/omf-resctl.yaml
perl -i.bak -pe "s/\:slice\:/\:slice\: $slicename/g" /etc/omf-resctl-5.4/omf-resctl.yaml
/etc/init.d/omf-resctl-5.4 restart

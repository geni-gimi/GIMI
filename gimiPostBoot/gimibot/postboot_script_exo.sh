#!/bin/bash

echo $1 > slice1
#echo $1 > /tmp/thisnodeslice
read -r slice<slice1
#read -r slice</tmp/thisnodeslice
slicename=$(echo $slice | cut -f4 -d+)
#echo $slicename
echo $2 > host3
#echo $self.Name() > /tmp/thisnodename
#read -r host</tmp/thisnodename
read -r host<host3
#echo $host

#host1=$(echo $host | cut -f1 -d.)
#/bin/hostname -F /etc/hostname
hostname $host
curl http://emmy9.casa.umass.edu/pingWrap.rb -o /root/pingWrap.rb
chmod +x /root/pingWrap.rb

curl http://emmy9.casa.umass.edu/omf-resctl.yaml -o /etc/omf-resctl-5.4/omf-resctl.yaml
perl -i.bak -pe "s/\:slice\:/\:slice\: $slicename/g" /etc/omf-resctl-5.4/omf-resctl.yaml
/etc/init.d/omf-resctl-5.4 restart

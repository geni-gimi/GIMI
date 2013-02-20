#defProperty('source1', 'omf.nicta.node11', 'ID of a resource')
#defProperty('source2', 'omf.nicta.node13', 'ID of a resource')
#defProperty('target', 'emmy9.casa.umass.edu/expect_wget_script.sh', 'download target1')
#defProperty('target1', 'emmy9.casa.umass.edu/expect_script.sh', 'download target2')

defGroup('Node1', "nodeA")
defGroup('Node2', "nodeB")
defGroup('Node3', "nodeC")
defGroup('Node4', "nodeD")
defGroup('Node5', "nodeE")


onEvent(:ALL_UP) do |event|
  wait 1
#  group('All').startApplications
  info 'Changing routing setup'

  group('Node1').exec("route add -net 192.168.1.0/24 gw 192.168.4.10")
  group('Node1').exec("route add -net 192.168.2.0/24 gw 192.168.4.10")
  group('Node1').exec("route add -net 192.168.3.0/24 gw 192.168.5.12")
  group('Node1').exec("route add -net 192.168.6.0/24 gw 192.168.5.12")
  group('Node1').exec("echo 1 >  /proc/sys/net/ipv4/ip_forward")

  group('Node2').exec("route add -net 192.168.3.0/24 gw 192.168.1.13")
  group('Node2').exec("route add -net 192.168.5.0/24 gw 192.168.4.11")
  group('Node2').exec("route add -net 192.168.6.0/24 gw 192.168.2.12")
  group('Node2').exec("echo 1 >  /proc/sys/net/ipv4/ip_forward")

  group('Node3').exec("route add -net 192.168.1.0/24 gw 192.168.3.13")
  group('Node3').exec("route add -net 192.168.4.0/24 gw 192.168.5.11")
  group('Node3').exec("echo 1 >  /proc/sys/net/ipv4/ip_forward")

  group('Node4').exec("route add -net 192.168.2.0/24 gw 192.168.3.12")
  group('Node4').exec("route add -net 192.168.4.0/24 gw 192.168.1.10")
  group('Node4').exec("route add -net 192.168.5.0/24 gw 192.168.3.12")
  group('Node4').exec("route add -net 192.168.6.0/24 gw 192.168.3.12")
  group('Node4').exec("echo 1 >  /proc/sys/net/ipv4/ip_forward")

  group('Node5').exec("route add -net 192.168.2.0/24 gw 192.168.6.12")
  group('Node5').exec("route add -net 192.168.1.0/24 gw 192.168.6.12")
  group('Node5').exec("route add -net 192.168.3.0/24 gw 192.168.6.12")
  group('Node5').exec("route add -net 192.168.4.0/24 gw 192.168.6.12")
  group('Node5').exec("route add -net 192.168.5.0/24 gw 192.168.6.12")

  info 'Routing setup finished'
#  puts "downloading experiment script"
#  allGroups.exec("wget emmy9.casa.umass.edu/script.sh")
#  puts "Execute command '/bin/sh expect_wget_script.sh' on all nodes"
#  allGroups.exec("sh /root/script.sh")
#  allGroups.startApplications
  wait 5
  info 'Stopping applications'
  allGroups.stopApplications
  wait 1
  Experiment.done
end


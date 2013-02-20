defProperty('theSender','nodeB','ID of sender node')
defProperty('theReceiver1', 'nodeE', "ID of receiver node")
defProperty('theReceiver2', 'nodeA', "ID of receiver node")
defProperty('theReceiver3', 'nodeD', "ID of receiver node")
defProperty('packetsize', 128, "Packet size (byte) from the sender node")
defProperty('bitrate', 2048, "Bitrate (bit/s) from the sender node")
defProperty('runtime', 40, "Time in second for the experiment is to run")

defGroup('Sender',property.theSender) do |node|
    options = { 'sample-interval' => 2, 'monitor_interface' => 'eth1 -i eth2 -i eth3' }
    node.addPrototype("system_monitor", options)
    node.addApplication("test:app:otg2") do |app|
        app.setProperty('udp:local_host', '192.168.2.10')
        app.setProperty('udp:dst_host', '192.168.6.14')
        app.setProperty('udp:dst_port', 3000)
        app.setProperty('cbr:size', property.packetsize)
        app.setProperty('cbr:rate', property.bitrate * 2)
        app.measure('udp_out', :samples => 1)
    end
    
    node.addApplication("test:app:otg2") do |app|
        app.setProperty('udp:local_host', '192.168.4.10')
        app.setProperty('udp:dst_host', '192.168.4.11')
        app.setProperty('udp:dst_port', 3000)
        app.setProperty('cbr:size', property.packetsize)
        app.setProperty('cbr:rate', property.bitrate * 2)
        app.measure('udp_out', :samples => 1)
    end
    
    node.addApplication("test:app:otg2") do |app|
        app.setProperty('udp:local_host', '192.168.1.10')
        app.setProperty('udp:dst_host', '192.168.1.13')
        app.setProperty('udp:dst_port', 3000)                                    
        app.setProperty('cbr:size', property.packetsize)                                            
        app.setProperty('cbr:rate', property.bitrate * 2)                                                    
        app.measure('udp_out', :samples => 1)                                                        
    end
end

defGroup('Receiver1',property.theReceiver1) do |node|
    options = { 'sample-interval' => 2 }
    node.addPrototype("system_monitor", options)

    node.addApplication("test:app:otr2") do |app|
        app.setProperty('udp:local_host', '192.168.6.14')
        app.setProperty('udp:local_port', 3000)
        app.measure('udp_in', :samples => 1)
    end
end

defGroup('Receiver2',property.theReceiver2) do |node|
    options = { 'sample-interval' => 2 }
    node.addPrototype("system_monitor", options)
    node.addApplication("test:app:otr2") do |app|
        app.setProperty('udp:local_host', '192.168.4.11')
        app.setProperty('udp:local_port', 3000)
        app.measure('udp_in', :samples => 1)
    end 
end

defGroup('Receiver3',property.theReceiver3) do |node|     
    options = { 'sample-interval' => 2 }
    node.addPrototype("system_monitor", options)
    node.addApplication("test:app:otr2") do |app|                    
        app.setProperty('udp:local_host', '192.168.1.13')
        app.setProperty('udp:local_port', 3000)                                
        app.measure('udp_in', :samples => 1)                                    
    end
end

onEvent(:ALL_UP_AND_INSTALLED) do |event|
    info "starting"
    wait 5
    allGroups.exec("ln -s /usr/local/bin/otr2 /usr/bin/otr2")
    allGroups.exec("ln -s /usr/local/bin/otg2 /usr/bin/otg2")
    allGroups.exec("ln -s /usr/local/bin/oml2-nmetrics /usr/bin/oml2-nmetrics")
    allGroups.startApplications
    info "All applications started..."
    wait property.runtime / 4
    property.packetsize = 256
    wait property.runtime / 4
    property.packetsize = 512
    wait property.runtime / 4
    property.packetsize = 1024
    wait property.runtime / 4
    allGroups.stopApplications
    info "All applications stopped." 
    Experiment.done
end


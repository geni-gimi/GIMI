defProperty('source1', "nodeA", "ID of a resource")
defProperty('source2', "nodeB", "ID of a resource")
defProperty('source3', "nodeC", "ID of a resource")
defProperty('source4', "nodeD", "ID of a resource")
defProperty('source5', "nodeE", "ID of a resource")

defProperty('sinkaddr11', '192.168.1.13', "Ping destination address")
defProperty('sinkaddr12', '192.168.3.13', "Ping destination address")
defProperty('sinkaddr13', '192.168.6.14', "Ping destination address")

defProperty('sinkaddr21', '192.168.6.14', "Ping destination address")

defProperty('sinkaddr41', '192.168.4.11', "Ping destination address")
defProperty('sinkaddr42', '192.168.5.11', "Ping destination address")
defProperty('sinkaddr43', '192.168.6.14', "Ping destination address")

defProperty('sinkaddr51', '192.168.5.11', "Ping destination address")
defProperty('sinkaddr52', '192.168.2.10', "Ping destination address")
defProperty('sinkaddr53', '192.168.3.13', "Ping destination address")

defApplication('ping_app', 'pingmonitor') do |a|
        a.path = "/root/pingWrap.rb"
        a.version(1, 2, 0)
        a.shortDescription = "Wrapper around ping"
        a.description = "ping application"
        a.defProperty('dest_addr', 'Address to ping', '-a', {:type => :string, :dynamic => false})
        a.defProperty('count', 'Number of times to ping', '-c', {:type => :integer, :dynamic => false})
        a.defProperty('interval', 'Interval between pings in s', '-i', {:type => :integer, :dynamic => false})
        
        a.defMeasurement('myping') do |m|
            m.defMetric('dest_addr',:string)
            m.defMetric('ttl',:int)
            m.defMetric('rtt',:float)
            m.defMetric('rtt_unit',:string)
        end
end

defGroup('Source1', property.source1) do |node|
      node.addApplication("ping_app") do |app|
          app.setProperty('dest_addr', property.sinkaddr11)
          app.setProperty('count', 30)
          app.setProperty('interval', 1)
          app.measure('myping', :samples => 1)
      end
      
      node.addApplication("ping_app") do |app|
          app.setProperty('dest_addr', property.sinkaddr12)
          app.setProperty('count', 30)
          app.setProperty('interval', 1)
          app.measure('myping', :samples => 1)
      end

      node.addApplication("ping_app") do |app|          
          app.setProperty('dest_addr', property.sinkaddr13)
          app.setProperty('count', 30)              
          app.setProperty('interval', 1)                  
          app.measure('myping', :samples => 1)
      end
end

defGroup('Source2', property.source1) do |node|
    node.addApplication("ping_app") do |app|              
        app.setProperty('dest_addr', property.sinkaddr21)        
        app.setProperty('count', 30)            
        app.setProperty('interval', 1)                
        app.measure('myping', :samples => 1)                  
    end                
end

defGroup('Source4', property.source3) do |node|
      node.addApplication("ping_app") do |app|
          app.setProperty('dest_addr', property.sinkaddr41)
          app.setProperty('count', 30)
          app.setProperty('interval', 1)
          app.measure('myping', :samples => 1)
      end

      node.addApplication("ping_app") do |app|
          app.setProperty('dest_addr', property.sinkaddr42)
          app.setProperty('count', 30)
          app.setProperty('interval', 1)
          app.measure('myping', :samples => 1)
      end

      node.addApplication("ping_app") do |app|
          app.setProperty('dest_addr', property.sinkaddr43)
          app.setProperty('count', 30)
          app.setProperty('interval', 1)
          app.measure('myping', :samples => 1)
      end
end

defGroup('Source5', property.source3) do |node|
          node.addApplication("ping_app") do |app|
              app.setProperty('dest_addr', property.sinkaddr51)
              app.setProperty('count', 30)
              app.setProperty('interval', 1)
              app.measure('myping', :samples => 1)
          end

          node.addApplication("ping_app") do |app|
              app.setProperty('dest_addr', property.sinkaddr52)
              app.setProperty('count', 30)
              app.setProperty('interval', 1)
              app.measure('myping', :samples => 1)
          end

          node.addApplication("ping_app") do |app|
              app.setProperty('dest_addr', property.sinkaddr53)
              app.setProperty('count', 30)
              app.setProperty('interval', 1)
              app.measure('myping', :samples => 1)
          end
end

onEvent(:ALL_UP_AND_INSTALLED) do |event|
      info "Starting the ping"
      allGroups.startApplications
      wait 60
      info "Stopping the ping"
      allGroups.stopApplications
      Experiment.done
end

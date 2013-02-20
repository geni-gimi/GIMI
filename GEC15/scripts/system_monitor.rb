defPrototype("system_monitor") do |p| 

  p.name = "System Monitor" 
  p.description = "A monitor that reports stats on the system's resource usage" 

  p.defProperty('monitor_cpu', 'Monitor the CPU usage', true)
  p.defProperty('monitor_memory', 'Monitor the Memory usage', true)
  p.defProperty('monitor_interface', 'Monitor the interface usage', 'eth1')
  p.defProperty('sample-interval', 'sample-interval', '1')
  #  p.defProperty(('sample-interval', 'Time between consecutive measurements [sec], default 1s', '-s', {:type => :integer, :dynamic => false}))

  p.addApplication("nmetrics_app") do |a|
    a.bindProperty('cpu', 'monitor_cpu')
    a.bindProperty('memory', 'monitor_memory')
    a.bindProperty('interface', 'monitor_interface')
    a.bindProperty('sample-interval', 'sample-interval')
    a.measure('cpu', :samples => 1)
    a.measure('memory', :samples => 1)
    a.measure('net_if', :samples => 1)
  end
end

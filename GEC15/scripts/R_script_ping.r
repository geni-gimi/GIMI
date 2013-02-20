library(RSQLite)
con <- dbConnect(dbDriver("SQLite"), dbname = "gimiXX-ping.sq3")
dbListTables(con)
dbReadTable(con,"pingmonitor_myping")

mydata1 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.4.10'")
rtt1 <- abs(mydata1$rtt)

mydata2 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.5.12'")
rtt2 <- abs(mydata2$rtt)

mydata3 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.4.11'")
rtt3 <- abs(mydata3$rtt)

mydata4 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.2.12'")
rtt4 <- abs(mydata4$rtt)

mydata5 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.1.13'")
rtt5 <- abs(mydata5$rtt)

mydata6 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.5.11'")
rtt6 <- abs(mydata6$rtt)

mydata7 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.2.10'")
rtt7 <- abs(mydata7$rtt)

mydata8 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.3.13'")
rtt8 <- abs(mydata8$rtt)

mydata9 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.6.14'")
rtt9 <- abs(mydata9$rtt)

mydata10 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.1.10'")
rtt10 <- abs(mydata10$rtt)

mydata11 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.3.12'")
rtt11 <- abs(mydata11$rtt)

mydata12 <- dbGetQuery(con, "select dest_addr, rtt from pingmonitor_myping where dest_addr='192.168.6.12'")
rtt12 <- abs(mydata12$rtt)

png(filename="gimi-ping.png", height=650, width=900,
 bg="white")
g_range <- range(0,rtt1,rtt2,rtt3,rtt4,rtt5,rtt6,rtt7,rtt8,rtt9,rtt10,rtt11,rtt12)

plot(rtt1,type="o",col="red",ylim= g_range, lty=2, xlab="Experiment Interval",ylab="RTT")
lines(rtt2,type="o",col="blue",xlab="Experiment Interval",ylab="Received Data")
lines(rtt3,type="o",col="green",xlab="Experiment Interval",ylab="Received Data")
lines(rtt4,type="o",col="purple",xlab="Experiment Interval",ylab="Received Data")
lines(rtt5,type="o",col="violetred",xlab="Experiment Interval",ylab="Received Data")
lines(rtt6,type="o",col="springgreen",xlab="Experiment Interval",ylab="Received Data")
lines(rtt7,type="o",col="skyblue",xlab="Experiment Interval",ylab="Received Data")
lines(rtt8,type="o",col="sienna",xlab="Experiment Interval",ylab="Received Data")
lines(rtt9,type="o",col="pink",xlab="Experiment Interval",ylab="Received Data")
lines(rtt10,type="o",col="yellow",xlab="Experiment Interval",ylab="Received Data")
lines(rtt11,type="o",col="thistle",xlab="Experiment Interval",ylab="Received Data")
lines(rtt12,type="o",col="orange",xlab="Experiment Interval",ylab="Received Data")

title(main="Ping: Round Trip Time", col.main="red", font.main=4)
legend("topright", g_range[4], legend=c("192.168.4.10","192.168.5.12","192.168.4.11","192.168.2.12","192.168.5.11","192.168.2.10","192.168.3.13","192.168.6.14","192.168.1.10","192.168.3.12","192.168.6.12"), cex=0.8,
   col=c("blue","red","green","purple","violetred","springgreen","skyblue","sienna","pink","yellow","thistle","orange"), pch=15:16:17:18:19:20:21:22:23:24:25:26, lty=1:2:3:4:5:6:7:8:9:10:11:12);

dev.off()








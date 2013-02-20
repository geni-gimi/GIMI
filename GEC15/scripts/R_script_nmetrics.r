
library(RSQLite)
con <- dbConnect(dbDriver("SQLite"), dbname = "gimiXX-otg-nmetrics.sq3")
dbListTables(con)
dbReadTable(con,"nmetrics_net_if")

mydata1 <- dbGetQuery(con, "select oml_sender_id, rx_bytes from nmetrics_net_if where oml_sender_id=1")
rx_bytes1 <- abs(mydata1$rx_bytes)
#plot(rx_bytes1, type="o", color="red", xlab="Experiment Interval", ylab="Received data")

mydata2 <- dbGetQuery(con, "select oml_sender_id, rx_bytes from nmetrics_net_if where oml_sender_id=2")
rx_bytes2 <- abs(mydata2$rx_bytes)

mydata3 <- dbGetQuery(con, "select oml_sender_id, rx_bytes from nmetrics_net_if where oml_sender_id=3")
rx_bytes3 <- abs(mydata3$rx_bytes)

mydata4 <- dbGetQuery(con, "select oml_sender_id, rx_bytes from nmetrics_net_if where oml_sender_id=4")
rx_bytes4 <- abs(mydata4$rx_bytes)

png(filename="gimi-nmetrics-eth.png", height=650, width=900,
 bg="white")
g_range <- range(0,rx_bytes1,rx_bytes2,rx_bytes3,rx_bytes4)

plot(rx_bytes1,type="o",col="red",ylim= g_range, lty=2, xlab="Experiment Interval",ylab="Received Data")
lines(rx_bytes2,type="o",col="blue",xlab="Experiment Interval",ylab="Received Data")
lines(rx_bytes3,type="o",col="green",xlab="Experiment Interval",ylab="Received Data")
lines(rx_bytes4,type="o",col="purple",xlab="Experiment Interval",ylab="Received Data")
title(main="nmetrics experiment on ExoGENI (Received Data)", col.main="red", font.main=4)
legend("bottomright", g_range[4], legend=c("interface1","interface2","interface3","interface4"), cex=0.8,
   col=c("blue","red","green","purple"), pch=21:22:23:24, lty=1:2:3:4);


dbListTables(con)
dbReadTable(con,"nmetrics_memory")

mydata1 <- dbGetQuery(con, "select oml_sender_id, used from nmetrics_memory where oml_sender_id=1")
used1 <- abs(mydata1$used)
#plot(rx_bytes1, type="o", color="red", xlab="Experiment Interval", ylab="Received data")

mydata2 <- dbGetQuery(con, "select oml_sender_id, used from nmetrics_memory where oml_sender_id=2")
used2 <- abs(mydata2$used)

mydata3 <- dbGetQuery(con, "select oml_sender_id, used from nmetrics_memory where oml_sender_id=3")
used3 <- abs(mydata3$used)

mydata4 <- dbGetQuery(con, "select oml_sender_id, used from nmetrics_memory where oml_sender_id=4")
used4 <- abs(mydata4$used)

png(filename="gimi-nmetrics-memory.png", height=650, width=900,
 bg="white")
g_range <- range(0,used1,used2,used3,used4)

plot(used1,type="o",col="red",ylim= g_range, lty=2, xlab="Experiment Interval",ylab="Used Memory")
lines(used2,type="o",col="blue",xlab="Experiment Interval",ylab="Used Memory")
lines(used3,type="o",col="green",xlab="Experiment Interval",ylab="Used Memory")
lines(used4,type="o",col="purple",xlab="Experiment Interval",ylab="Used Memory")
title(main="nmetrics experiment on ExoGENI (Used Memory)", col.main="red", font.main=4)
legend("bottomright", g_range[4], legend=c("interface1","interface2","interface3","interface4"), cex=0.8,
   col=c("blue","red","green","purple"), pch=21:22:23:24, lty=1:2:3:4);


dbListTables(con)
dbReadTable(con,"nmetrics_cpu")

mydata1 <- dbGetQuery(con, "select oml_sender_id, user from nmetrics_cpu where oml_sender_id=1")
user1 <- abs(mydata1$user)
#plot(rx_bytes1, type="o", color="red", xlab="Experiment Interval", ylab="Received data")

mydata2 <- dbGetQuery(con, "select oml_sender_id, user from nmetrics_cpu where oml_sender_id=2")
user2 <- abs(mydata2$user)

mydata3 <- dbGetQuery(con, "select oml_sender_id, user from nmetrics_cpu where oml_sender_id=3")
user3 <- abs(mydata3$user)

mydata4 <- dbGetQuery(con, "select oml_sender_id, user from nmetrics_cpu where oml_sender_id=4")
user4 <- abs(mydata4$user)

png(filename="gimi-nmetrics-cpu.png", height=650, width=900,
 bg="white")
g_range <- range(0,user1,user2,user3,user4)

plot(user1,type="o",col="red",ylim= g_range, lty=2, xlab="Experiment Interval",ylab="user CPU")
lines(user2,type="o",col="blue",xlab="Experiment Interval",ylab="user CPU")
lines(user3,type="o",col="green",xlab="Experiment Interval",ylab="user CPU")
lines(user4,type="o",col="purple",xlab="Experiment Interval",ylab="user CPU")
title(main="nmetrics experiment on ExoGENI (user CPU)", col.main="red", font.main=4)
legend("bottomright", g_range[4], legend=c("interface1","interface2","interface3","interface4"), cex=0.8,
   col=c("blue","red","green","purple"), pch=21:22:23:24, lty=1:2:3:4);


dev.off()



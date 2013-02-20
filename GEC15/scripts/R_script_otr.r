
library(RSQLite)
con <- dbConnect(dbDriver("SQLite"), dbname = "gimiXX-otg-nmetrics.sq3")
dbListTables(con)
dbReadTable(con,"otr2_udp_in")

mydata1 <- dbGetQuery(con, "select oml_sender_id, pkt_length from otr2_udp_in where src_host='192.168.4.10'")
pkt_length <- mydata1$pkt_length
#plot(rx_bytes1, type="o", color="red", xlab="Experiment Interval", ylab="Received data")


png(filename="gimi-otg1.png", height=650, width=900,
 bg="white")
g_range <- range(0,pkt_length)

plot(pkt_length,type="o",col="red",ylim= g_range, lty=2, xlab="Experiment Interval",ylab="Packet Size")

title(main="Received packet size with sender address 192.168.4.10", col.main="red", font.main=4)
legend("bottomright", g_range[1], legend=c("interface1"), cex=0.8,
   col=c("blue"), pch=21, lty=1);

dev.off()

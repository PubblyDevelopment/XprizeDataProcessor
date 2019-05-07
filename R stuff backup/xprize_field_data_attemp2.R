library("ggplot2")

data <- read.csv(file="/Users/wallis/PycharmProjects/XprizeDataProcessor/RESULTS_notimes.csv")

table(data$uniqueID)
plot(data$villageNum, data$isEQ)
plot(data$category, mean(data$time))

agg = aggregate(data, by = list(data$category), FUN=mean)
agg = aggregate(data, by = list(data$villageNum), FUN=sum)

table(data$village, data$EQ)
p<-ggplot(data, aes(x=villageNum, y=EQ, fill=EQ)) +
   geom_bar(stat='identity') + 
   labs(x="Village #", y="", title="Total Activity Count 1/11 -> 1/25") +
   guides(title="fart")
p
View(table(data$filename, data$uniqueID))

x <- sort(table(data$filename),decreasing=T)
x
write.csv(x,"/Users/wallis/Dev/XprizeDataProcessing/freq.csv",quote=F)

table(data$EQ)
pie(table(data$EQ), main="Is it an EQ file?")
x <- c(27739, 215554)
piep <- round(100*x/sum(x), 1)
pie(x, labels = piep, main="Is it an EQ file?", legend("topright", c("Yes","No")))
piep <- paste(piep,"%",sep="")
pie(x, labels = piep, main = "Is it an EQ file?", col = rainbow(length(x)))
legend("topright", c("Yes","No"), cex = 0.8,
       fill = rainbow(length(x)))

# Export to CSV
write.table(table(data$filename), "/Users/wallis/Dev/XprizeDataProcessing/accEQs.txt", sep="," )

View(table(data$villageNum))

plot(data$weekNum, main="Total Number of Files Accessed Per Week")
agg = aggregate(data, by = list(data$uniqueID), FUN=sum)
agg

agg = aggregate(data, by = list(data$time), FUN=sum)

agg$filename
length(data$villageNum)
length(data$isEQ)

plot(data$category, main="# Activity Accesses per Category 1/11 - 1/25")

plot(data$villageNum, agg$time)
agg$Group.1

warnings()

table(agg$Group.1)

p<-ggplot(data=agg, aes(x=Group.1, y=time, fill=Group.1)) + 
  geom_bar(stat="identity") + theme_minimal()  + theme(legend.position="none") +
  labs(x="Category", y="Time (in minutes)", title="Mean Time Spent per Acct per Category in One Week")
p
  warnings()

agg = aggregate(data, by=list(data$tabID), FUN=sum)

pie <- p+coord_polar("y", start=0)
pie

View(table(data$uniqueID))

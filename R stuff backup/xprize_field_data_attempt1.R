library("ggplot2")

data <- read.csv(file="/Users/wallis/Dev/XprizeDataProcessing/result.txt")
data$totalTime
boxplot(data$minutes, horizontal=TRUE, range=2, outline=FALSE, main="Total Tablet Usage in One Week", xlab="minutes spent in each activity (extreme values removed)")
mean(data$totalTime)
boxplot(data$totalTime, horizontal=TRUE, outline=FALSE, main="Total Tablet Usage in One Week per User Account\n(outliers removed)", xlab="minutes")
max(data$totalTime)/60
plot(data$userID, data$totalTime)

plot(data$time/60,data$subject)
barplot(data$time/222/60,names.arg=c("1","2","3","4","5"), xlab="Account Number",main="Total Time Spent in a Week", ylab="hours per user")
data
max(data$time)/60

barplot(data$time/222/60)
hourtime = data$time/60/222
p<-ggplot(data=data, aes(x=subject, y=hourtime, fill=subject)) + 
  geom_bar(stat="identity") + theme_minimal() +
  labs(title="Time Spent in One Week by Subject Per Usr Acct",y="Average Hours Spent", x="") 

View(data$filename)
plot(data$filename)
t = table(data$filename)
prop.table(t)
View(t)
